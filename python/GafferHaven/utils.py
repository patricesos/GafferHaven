import json
import os
import urllib.request
import platform
import subprocess

from PySide2.QtGui import QPixmap

# Query the Polyhaven api https://github.com/Poly-Haven/Public-API


def haven_api_query(arguments):
    # Setting headers to prevent 403 error
    user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    url = "https://api.polyhaven.com/" + arguments
    headers = {
        "User-Agent": user_agent,
    }
    # Query the api
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)

    data = response.read()  # Store the json response as dict
    json_data = json.loads(data)
    return json_data


# Make all folders in the path unless they already exist
def make_folder(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path, mode=0o777, exist_ok=True)


# Download file from web
def download_hdri(source, target):
    """
    Download hdris from source
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
        }
        request_ = urllib.request.Request(source, None, headers)
        response = urllib.request.urlopen(request_)

        with open(target, "wb") as out_file:  # create a new file and write the image
            out_file.write(response.read())
    except Exception as e:
        print(f"Failed to download {source} to {target}")
        print(e.__class__)
        print(e.reason)


# save dict as json file
def dump_to_json(filepath, dictonary):
    with open(filepath, "w") as f:
        json.dump(dictonary, f)


# Load json file as dict
def load_json_dict(file_path):
    try:
        with open(file_path, "r") as j:
            return json.loads(j.read())
    except Exception as e:
        print(f"Could not load {file_path}, {e}")
        return {}


# Adds item from 2nd lists to the 1st one except if they already exist there
def merge_into_list(target_list, source_list):
    out = target_list
    for i in source_list:
        if i not in target_list:
            out.append(i)
    return out


# Opens the file/folder in OS's file borwser
def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


# Removes all items in layout
def clear_layout(my_layout):
    index = my_layout.count() - 1
    while index >= 0:
        myWidget = my_layout.itemAt(index).widget()
        if myWidget is not None:
            myWidget.setParent(None)
        else:
            my_layout.removeItem(my_layout.itemAt(index))
        index -= 1


# creates QPixmap from url on an image
def pixmap_from_URL(url):
    data = urllib.request.urlopen(url).read()
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    return pixmap


# creates QPixmap from icon inside the Gaffer's graphics folder
def pixmap_gaffer_icon(name):
    path = os.environ.get("GAFFER_ROOT") + "/graphics/" + name
    return QPixmap(path)
