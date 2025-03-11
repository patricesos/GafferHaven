import os

import Gaffer
import GafferCycles
import GafferHaven
import GafferUI
import imath

Gaffer.Metadata.registerValue(
    GafferCycles.CyclesShader,
    "layout:activator:textureIsEnv",
    lambda node: node["name"].getValue() == "environment_texture",
)

Gaffer.Metadata.registerValue(
    GafferCycles.CyclesShader,
    "layout:customWidget:browseHDRI:widgetType",
    "GafferHaven.guiTest.BrowseButton",
)

Gaffer.Metadata.registerValue(
    GafferCycles.CyclesShader,
    "layout:customWidget:browseHDRI:visibilityActivator",
    "textureIsEnv",
)


if "ARNOLD_ROOT" in os.environ:
    import GafferArnold

    Gaffer.Metadata.registerValue(
        GafferArnold.ArnoldShader,
        "layout:activator:shaderIsImage",
        lambda node: node["name"].getValue() == "image",
    )
    Gaffer.Metadata.registerValue(
        GafferArnold.ArnoldShader,
        "layout:customWidget:browseHDRI:widgetType",
        "GafferHaven.guiTest.BrowseButton",
    )
    Gaffer.Metadata.registerValue(
        GafferArnold.ArnoldShader,
        "layout:customWidget:browseHDRI:section",
        "Settings",
    )
    Gaffer.Metadata.registerValue(
        GafferArnold.ArnoldShader,
        "layout:customWidget:browseHDRI:visibilityActivator",
        "shaderIsImage",
    )
