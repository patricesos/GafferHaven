import GafferHaven
import Gaffer, GafferUI, os, imath
import GafferCycles


import GafferCycles
Gaffer.Metadata.registerValue(
	GafferCycles.CyclesShader,
	"layout:activator:textureIsEnv", lambda node : node["name"].getValue() == "environment_texture"
) 
Gaffer.Metadata.registerValue(
	GafferCycles.CyclesShader, "layout:customWidget:browseHDRI:widgetType", "GafferHaven.gui.BrowseButton",
)
Gaffer.Metadata.registerValue(
<<<<<<< Updated upstream
	GafferCycles.CyclesShader, "layout:customWidget:browseHDRI:section", "Settings",
=======
    GafferCycles.CyclesShader,
    "layout:customWidget:browseHDRI:widgetType",
    "GafferHaven.guiTest.BrowseButton",
>>>>>>> Stashed changes
)
Gaffer.Metadata.registerValue(
	GafferCycles.CyclesShader,
	"layout:customWidget:browseHDRI:visibilityActivator", "textureIsEnv"
)


if "ARNOLD_ROOT" in os.environ:
	import GafferArnold
	Gaffer.Metadata.registerValue(
		GafferArnold.ArnoldShader,
		"layout:activator:shaderIsImage", lambda node : node["name"].getValue() == "image"
	) 
	Gaffer.Metadata.registerValue(
		GafferArnold.ArnoldShader, "layout:customWidget:browseHDRI:widgetType", "GafferHaven.gui.BrowseButton",
	)
	Gaffer.Metadata.registerValue(
		GafferArnold.ArnoldShader, "layout:customWidget:browseHDRI:section", "Settings",
	)
	Gaffer.Metadata.registerValue(
		GafferArnold.ArnoldShader,
		"layout:customWidget:browseHDRI:visibilityActivator", "shaderIsImage"
	)



<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes
