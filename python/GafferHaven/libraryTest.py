import json
import os
import pathlib
import ssl
import urllib.request

from .utils import *  # noqa: F403


# library stores both local and web assets
class Library:
    def __init__(self):
        self.lib_path = key = os.getenv("HAVENLIBRARY")
        self.local_hdris_path = os.path.join(self.lib_path, "hdris/downloaded")
        self.local_cache_path = os.path.join(self.lib_path, "hdris/cache")
        self.assets = {}
        self.assets["local_hdris"] = []
        self.assets["web_hdris"] = []
        self.categories = {}
        self.categories["local_hdris"] = []
        self.categories["web_hdris"] = []
        make_folder(self.local_hdris_path)
        make_folder(self.local_cache_path)
        self.reload_local_db()

    def reload_local_db(self):
        self.assets["local_hdris"] = []
        dirs = os.listdir(self.local_hdris_path)
        for d in dirs:
            hdri_info = {}
            hdri = Hdri(d, self, True, hdri_info)
            self.assets["local_hdris"].append(hdri)
            self.categories["local_hdris"] = merge_into_list(
                self.categories["local_hdris"], hdri.categories
            )

    def reload_web(self):
        self.assets["web_hdris"] = []
        data = haven_api_query("assets?t=hdris")
        for key, hdri_info in data.items():
            hdri = Hdri(key, self, False, hdri_info)
            self.assets["web_hdris"].append(hdri)
            self.categories["web_hdris"] = merge_into_list(
                self.categories["web_hdris"],
                hdri.categories,
                # self.categories["local_hdris"], hdri.categories
            )


class Hdri:
    def __init__(self, hdri_id, library, local, hdri_info):
        self.local = local
        self.hdri_id = hdri_id
        self.library = library
        self.hdri_info = hdri_info
        self.resolutions_downloaded = []

        if local:
            self.thumbnail = os.path.join(
                library.local_hdris_path, self.hdri_id, self.hdri_id + ".webp"
            )
            self.hdri_info = load_json_dict(
                os.path.join(
                    self.library.local_hdris_path, self.hdri_id, self.hdri_id + ".json"
                )
            )
        else:
            self.thumbnail = self.cache_thumbnail()

        self.get_resolutions_dowloaded()

        if "categories" in self.hdri_info.keys():
            self.categories = self.hdri_info["categories"]
        else:
            self.categories = []

    def get_file_path(self, resolution):
        return os.path.join(
            self.library.local_hdris_path,
            self.hdri_id,
            self.hdri_id + "_" + resolution + ".exr",
        )

    def get_resolutions_dowloaded(self):
        local_folder = self.library.local_hdris_path + "/" + self.hdri_id + "/"
        if os.path.isdir(local_folder):
            for file in os.listdir(local_folder):
                if file.endswith(".exr"):
                    self.resolutions_downloaded.append(
                        file.rsplit("_")[-1].rsplit(".")[0]
                    )

    def get_resolutions_available(self):
        data = haven_api_query("files/" + self.hdri_id)
        result = {}
        for resolution, files in data["hdri"].items():
            if "exr" in files.keys():
                result[resolution] = files["exr"]["url"]
        return result

    def set_hdri(self, resolution, node):
        # Set map path and resolution on the light node in Gaffer
        node_type = node.typeName()
        # Cycles
        if node_type == "GafferCycles::CyclesShader":
            node["parameters"]["filename"].setValue(
                self.get_file_path(resolution).replace(
                    self.library.local_hdris_path, "${HAVENLIBRARY}/hdris/downloaded"
                )
            )
            # node['parameters']['map_resolution'].setValue(self.get_map_resolution(resolution))
        # Arnold
        elif node_type == "GafferArnold::ArnoldShader":
            node["parameters"]["filename"].setValue(
                self.get_file_path(resolution).replace(
                    self.library.local_hdris_path, "${HAVENLIBRARY}/hdris/downloaded"
                )
            )

    def download_and_use(self, resolution, node, dowload_link):
        # Download .exr
        target_exr_path = self.get_file_path(resolution)
        make_folder(os.path.join(self.library.local_hdris_path, self.hdri_id))
        download_hdri(dowload_link, target_exr_path)

        # Download Thumbnail
        thumb_path = os.path.join(
            self.library.local_hdris_path, self.hdri_id, self.hdri_id + ".webp"
        )
        if not os.path.isfile(thumb_path):
            download_hdri(
                "https://cdn.polyhaven.com/asset_img/thumbs/"
                + self.hdri_id
                + ".png?height=480",
                thumb_path,
            )

        # Store hdri_info dict
        json_path = os.path.join(
            self.library.local_hdris_path, self.hdri_id, self.hdri_id + ".json"
        )
        dump_to_json(json_path, self.hdri_info)

        # Set map path and resolution on the light node in Gaffer
        self.set_hdri(resolution, node)

    def cache_thumbnail(self):
        cached_path = os.path.join(
            self.library.local_cache_path, self.hdri_id + ".webp"
        )
        if not os.path.isfile(cached_path):
            download_hdri(
                "https://cdn.polyhaven.com/asset_img/thumbs/"
                + self.hdri_id
                + ".png?height=180",
                cached_path,
            )
        return cached_path

    def get_map_resolution(self, resolution):
        available_resolutions = {
            "1k": 1024,
            "2k": 2048,
            "4k": 4096,
            "8k": 8192,
            "16k": 16384,
        }  # noqa: E501
        if resolution not in available_resolutions.keys():
            return 1024
        else:
            return available_resolutions[resolution]
