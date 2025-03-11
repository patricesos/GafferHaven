<<<<<<< Updated upstream:python/GafferHaven/gui.py
import Gaffer, GafferUI
import os, platform, subprocess, ssl, urllib.request
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QTabWidget, QScrollArea, QGridLayout, QPushButton, QFormLayout, QLabel, QComboBox
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter,QColor,QPixmap
from .library import Library
=======
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import (
    QComboBox,
    QFormLayout,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QTabWidget,
    QVBoxLayout,
    QWidget,
    QApplication,
)

import Gaffer
import GafferUI

from .utils import *  # noqa: F403
from .libraryTest import Library
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

class MainWindow(QWidget):
<<<<<<< Updated upstream:python/GafferHaven/gui.py
		def __init__(self, lib, origin_node):
				super(MainWindow, self).__init__()
				self.origin_node = origin_node # The node in gaffer from which the window was launched (Light)
				self.icon_width = 240
				self.icon_height = self.icon_width*0.75
				self.h_icons = 3 # icons per row
				self.infoW = 700 # Width of the info box
				self.lib = lib
				self.selection = []
				self.category_filter = "All"
				self.build()
				self.setWindowTitle("HDRI browser")

		def build(self):
				self.selected = None

				self.setFixedSize(self.h_icons*self.icon_width*1.1 + self.infoW, 800)
				self.setStyleSheet("background-color:#444444;color: white;")
				self.hbox = QHBoxLayout()
								
				self.left_side = QWidget()
				self.left_side_vbox = QVBoxLayout()
				self.left_side.setLayout(self.left_side_vbox)
=======
    def __init__(self, library, node):
        # def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("HDRI browser")
        self.setStyleSheet("background-color:#444444;color: white;")

        self.node = node
        self.icon_width = 240
        self.icon_height = self.icon_width * 0.75
        self.icons_per_row = 3  # icons per row
        self.info_box_width = 700  # Width of the info box
        self.library = library
        self.selection = []
        self.category_filter = "All"

        self.setFixedSize(
            self.icons_per_row * self.icon_width * 1.1 + self.info_box_width, 800
        )

        self.setup_ui()

    def setup_ui(self):
        self.selected = None
        self.hor_box = QHBoxLayout()
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

				self.top_bar = QWidget()
				self.top_bar_vbox = QHBoxLayout()
				self.top_bar.setLayout(self.top_bar_vbox)
				self.top_bar_vbox.addStretch()
				self.category_cb = CategoriesComboBox(self)
				self.top_bar_vbox.addWidget(QLabel("category: "))
				self.top_bar_vbox.addWidget(self.category_cb)
				self.left_side_vbox.addWidget(self.top_bar)

<<<<<<< Updated upstream:python/GafferHaven/gui.py
				self.local_page = AssetGridBox(self,"local_hdris")
				self.web_page = AssetGridBox(self,"web_hdris")
=======
        self.top_bar = QWidget()
        self.top_bar_vbox = QHBoxLayout()
        self.top_bar.setLayout(self.top_bar_vbox)
        # self.top_bar_vbox.addStretch()

        self.category_cbx = CategoriesComboBox(self)
        self.top_bar_vbox.addWidget(QLabel("category: "))
        self.top_bar_vbox.addWidget(self.category_cbx)
        self.left_side_vbox.addWidget(self.top_bar)
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

				self.tabs = QTabWidget()
				self.tabs.setFixedSize(self.h_icons*self.icon_width*1.1, 780)
				self.tabs.addTab(self.local_page, "Downloaded")
				self.tabs.addTab(self.web_page, "Web")
				self.tabs.currentChanged.connect(self.on_tab_change)
				self.left_side_vbox.addWidget(self.tabs)

<<<<<<< Updated upstream:python/GafferHaven/gui.py
				self.hbox.addWidget(self.left_side)

				self.info_box = InfoBox(self)
				self.hbox.addWidget(self.info_box)
				
				self.category_cb.refresh()
				self.setLayout(self.hbox)
				self.activateWindow()
				self.show()
				self.activateWindow()
=======
        self.tabs = QTabWidget()
        self.tabs.setFixedSize(self.icons_per_row * self.icon_width * 1.1, 780)
        self.tabs.addTab(self.local_page, "Downloaded")
        self.tabs.addTab(self.web_page, "Web")
        self.left_side_vbox.addWidget(self.tabs)
        self.tabs.currentChanged.connect(self.on_tab_change)

        self.hor_box.addWidget(self.left_side)

        self.info_box = InfoBox(self)
        self.hor_box.addWidget(self.info_box)

        self.category_cbx.refresh()
        self.setLayout(self.hor_box)
        self.activateWindow()
        self.show()
        self.activateWindow()

    def on_tab_change(self, tabIndex):
        if tabIndex == 0:
            self.library.reload_local_db()
            self.local_page.refresh()
            self.category_cbx.refresh()

        if tabIndex == 1:
            self.library.reload_web()
            self.web_page.refresh()
            self.category_cbx.refresh()
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

		def on_tab_change(self,tabIndex):
			if (tabIndex==0):
				self.lib.reload_local()
				self.local_page.refresh()
				self.category_cb.refresh()
			if (tabIndex==1):
				self.lib.reload_web()
				self.web_page.refresh()
				self.category_cb.refresh()

class CategoriesComboBox(QComboBox):
		def __init__(self,mainWindow):
			super(CategoriesComboBox, self).__init__()
			self.main_window = mainWindow
			self.setFixedWidth(150)
			self.currentTextChanged.connect(self.on_changed)

<<<<<<< Updated upstream:python/GafferHaven/gui.py
		def refresh(self):
			self.clear()
			self.addItem("All")
			categories = []
			if (self.main_window.tabs.currentIndex() == 0):
				categories = self.main_window.lib.categories["local_hdris"]
			elif (self.main_window.tabs.currentIndex() == 1):
				categories = self.main_window.lib.categories["web_hdris"]
			for c in categories:
				self.addItem(c)
=======
    def refresh(self):
        self.clear()
        self.addItem("All")

        categories = []
        if self.main_window.tabs.currentIndex() == 0:
            categories = self.main_window.library.categories["local_hdris"]
        elif self.main_window.tabs.currentIndex() == 1:
            categories = self.main_window.library.categories["web_hdris"]

        for c in categories:
            self.addItem(c)

    def on_changed(self, value):
        self.main_window.category_filter = value
        if self.main_window.tabs.currentIndex() == 0:
            self.main_window.local_page.refresh()
        elif self.main_window.tabs.currentIndex() == 1:
            self.main_window.web_page.refresh()
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

		def on_changed(self, value):
			self.main_window.category_filter = value;
			if (self.main_window.tabs.currentIndex() == 0):
				self.main_window.local_page.refresh()
			elif (self.main_window.tabs.currentIndex() == 1):
				self.main_window.web_page.refresh()

class AssetGridBox(QWidget):
<<<<<<< Updated upstream:python/GafferHaven/gui.py
		def __init__(self,main_window,category):
			super(AssetGridBox, self).__init__()
			self.main_window = main_window
			self.category = category
			self.build()

		def build(self):
			self.vbox = QVBoxLayout()
			self.page = QWidget()
			self.scroll = QScrollArea()
			self.scroll.setStyleSheet("background-color:#555555;")
			self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
			self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
			self.scroll.setWidgetResizable(True)
			self.scroll.setWidget(self.page)
			self.grid = QGridLayout()
			self.page.setLayout(self.grid)
			self.vbox.addWidget(self.scroll)
			self.setLayout(self.vbox)
			self.refresh()
=======
    def __init__(self, main_window, category):
        super(AssetGridBox, self).__init__()
        self.main_window = main_window
        self.category = category
        self.setup_ui()

    def setup_ui(self):
        self.vertical_box = QVBoxLayout()
        self.hdris_grid_widget = QWidget()
        self.scroll_area = QScrollArea()
        self.scroll_area.setStyleSheet("background-color:#555555;")
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.hdris_grid_widget)

        self.grid = QGridLayout()
        self.hdris_grid_widget.setLayout(self.grid)
        self.vertical_box.addWidget(self.scroll_area)
        self.setLayout(self.vertical_box)
        self.refresh()

    def refresh(self):
        # populate with assets
        clear_layout(self.grid)
        i = 0
        for selected_hdri in self.main_window.library.assets[self.category]:
            if (
                self.main_window.category_filter in selected_hdri.categories
                or self.main_window.category_filter == "All"
            ):
                icon = assetIcon(selected_hdri, self.main_window)
                row = i / self.main_window.icons_per_row
                col = i % self.main_window.icons_per_row
                self.grid.addWidget(icon, row, col)
                self.grid.setColumnMinimumWidth(col, self.main_window.icon_width)
                self.grid.setRowMinimumHeight(row, self.main_window.icon_height)
                self.grid.setColumnStretch(self.main_window.icons_per_row + 1, 1)
                self.grid.setRowStretch(i / self.main_window.icons_per_row + 1, 1)
                i += 1
        self.update()
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

		def refresh(self):
			# populate with assets
			clear_layout(self.grid)
			i = 0
			for hdri in self.main_window.lib.assets[self.category]:
				if ( self.main_window.category_filter in hdri.categories or self.main_window.category_filter=="All" ):
					icon = assetIcon(hdri,self.main_window)
					row = (i/self.main_window.h_icons)
					col = i%self.main_window.h_icons
					self.grid.addWidget(icon, row, col)
					self.grid.setColumnMinimumWidth(col, self.main_window.icon_width)
					self.grid.setRowMinimumHeight(row, self.main_window.icon_height)
					self.grid.setColumnStretch(self.main_window.h_icons+1, 1)
					self.grid.setRowStretch(i/self.main_window.h_icons+1, 1)
					i += 1
			self.update()

class assetIcon(QPushButton):
		def __init__(self,asset, mainWindow):
				super(assetIcon, self).__init__()
				self.asset = asset
				self.main_window = mainWindow
				self.selected = 0
				self.setFixedSize(self.main_window.icon_width,self.main_window.icon_height)
				self.setText(asset.id)

				#set thumbnail image
				if os.path.isfile(self.asset.thumbnail):
					self.style = "border-image: url(" + self.asset.thumbnail + ");background-repeat: no-repeat;border: 2px solid white;border-radius: 5px;text-align:bottom;font: bold 12px;color: white;padding-bottom: 160px;"
					self.setStyleSheet(self.style)

				self.clicked.connect(self.on_clicked)
				
		def on_clicked(self):
				self.main_window.selected = self.asset
				self.main_window.info_box.refresh()
				self.main_window.info_box.update()


class InfoBox(QWidget):
<<<<<<< Updated upstream:python/GafferHaven/gui.py
		def __init__(self,mainWindow):
				super(InfoBox, self).__init__()
				self.main_window = mainWindow
				self.build()
		def build(self):
			self.vbox = QVBoxLayout()

			# The Preview image
			self.image = QLabel()
			self.image.setFixedSize(640, 480)
			self.image.setAlignment(Qt.AlignCenter)
			self.vbox.addWidget(self.image)
			# The Name
			self.label = QLabel()
			self.label.setStyleSheet("font: bold 20px;color: white;padding-left: 20px;padding-top: 8px;background-color: rgb(50,50,50)")
			self.label.setAlignment(Qt.AlignVCenter)
			self.label.setFixedSize(640, 40)
			self.vbox.addWidget(self.label)
			# Details
			self.details_widget = QWidget()
			self.details_layout = QFormLayout()
			self.details_widget.setLayout(self.details_layout)
			self.details_widget.setStyleSheet("font: 12px;color: white;border: 5px;padding-left: 20px;padding-top: 5px")
			self.vbox.addWidget(self.details_widget)
			# The row with resolution buttons
			self.resolutions_box = QWidget();
			self.resolutions_box_layout= QHBoxLayout()
			self.resolutions_box.setLayout(self.resolutions_box_layout)
			self.vbox.addWidget(self.resolutions_box)

			self.setLayout(self.vbox)
		
		def refresh(self):
			hdri = self.main_window.selected
			if hdri != None:

				# The preview image
				if hdri.local:
					pixmap = QPixmap( hdri.thumbnail)
				else:
					pixmap = pixmap_from_URL("https://cdn.polyhaven.com/asset_img/thumbs/"+hdri.id+".png?height="+str(700*0.75))
				pixmap = pixmap.scaled(640, 480)
				self.image.setPixmap(pixmap)

				# The Name label
				name = hdri.id
				if ("name" in hdri.info.keys()):
					name = hdri.info["name"]
				self.label.setText(name)
				self.label.setAlignment(Qt.AlignLeft)

				# Details
				details_to_show = ["authors","tags","categories","whitebalance","envs_cap"]
				clear_layout(self.details_layout)
				for key in details_to_show:
					if key in hdri.info.keys():
						text = hdri.info[key]
						if (type(text) is list):
							text = ", ".join(text)
						elif (type(text) is dict):
							text = str(text).replace("{","").replace("}","").replace("'","")
						self.details_layout.addRow(key, QLabel(str(text)))

				# Web link
				self.weblink = QLabel('''<a href='https://polyhaven.com/a/{}'>https://polyhaven.com/a/{}</a>'''.format(hdri.id,hdri.id))
				self.weblink.setOpenExternalLinks(True)
				self.details_layout.addRow("Web", self.weblink)
=======
    def __init__(self, mainWindow):
        super(InfoBox, self).__init__()
        self.main_window = mainWindow
        self.setup_ui()

    def setup_ui(self):
        self.vertical_box = QVBoxLayout()

        # The Preview preview_view
        self.preview_view = QLabel()
        self.preview_view.setFixedSize(640, 480)
        self.preview_view.setAlignment(Qt.AlignCenter)
        self.vertical_box.addWidget(self.preview_view)

        # The Name
        self.label = QLabel()
        self.label.setStyleSheet(
            "font: bold 20px;color: white;padding-left: 20px;padding-top: 8px;background-color: rgb(50,50,50)"  # noqa: E501
        )
        self.label.setAlignment(Qt.AlignVCenter)
        self.label.setFixedSize(640, 40)
        self.vertical_box.addWidget(self.label)

        # Details
        self.details_widget = QWidget()
        self.details_layout = QFormLayout()
        self.details_widget.setLayout(self.details_layout)
        self.details_widget.setStyleSheet(
            "font: 12px;color: white;border: 5px;padding-left: 20px;padding-top: 5px"
        )
        self.vertical_box.addWidget(self.details_widget)

        # The row with resolution buttons
        self.resolutions_widget = QWidget()
        self.resolutions_box_layout = QHBoxLayout()
        self.resolutions_widget.setLayout(self.resolutions_box_layout)
        self.vertical_box.addWidget(self.resolutions_widget)

        self.setLayout(self.vertical_box)

    def refresh(self):
        selected_hdri = self.main_window.selected
        if selected_hdri is not None:
            # The preview preview_view
            if selected_hdri.local:
                pixmap = QPixmap(selected_hdri.thumbnail)
            else:
                pixmap = pixmap_from_URL(
                    "https://cdn.polyhaven.com/asset_img/thumbs/"
                    + selected_hdri.id
                    + ".png?height="
                    + str(700 * 0.75)
                )
            pixmap = pixmap.scaled(640, 480)
            self.preview_view.setPixmap(pixmap)

            # The Name label
            name = selected_hdri.id
            if "name" in selected_hdri.info.keys():
                name = selected_hdri.info["name"]
            self.label.setText(name)
            self.label.setAlignment(Qt.AlignLeft)

            # Details
            details_to_show = [
                "authors",
                "tags",
                "categories",
                "whitebalance",
                "envs_cap",
            ]
            clear_layout(self.details_layout)
            for key in details_to_show:
                if key in selected_hdri.info.keys():
                    text = selected_hdri.info[key]
                    if type(text) is list:
                        text = ", ".join(text)
                    elif type(text) is dict:
                        text = (
                            str(text).replace("{", "").replace("}", "").replace("'", "")
                        )
                    self.details_layout.addRow(key, QLabel(str(text)))

            # Web link
            self.weblink = QLabel(
                """<a href='https://polyhaven.com/a/{}'>https://polyhaven.com/a/{}</a>""".format(
                    selected_hdri.id, selected_hdri.id
                )
            )
            self.weblink.setOpenExternalLinks(True)
            self.details_layout.addRow("Web", self.weblink)

            # Download/Use buttons
            clear_layout(self.resolutions_box_layout)
            selected_hdri.get_resolutions_dowloaded()
            resolutions_available = selected_hdri.get_resolutions_available()
            for r in sorted(resolutions_available.keys()):
                if r in selected_hdri.resolutions_downloaded:
                    btn = ResolutionIcon(r, self.main_window, True, None)
                else:
                    btn = ResolutionIcon(
                        r, self.main_window, False, resolutions_available[r]
                    )
                self.resolutions_box_layout.addWidget(btn, 0, Qt.AlignLeft)
            self.resolutions_box_layout.addStretch()

            # Open folder button
            if selected_hdri.local:
                open_folder_button = FolderIcon(self.main_window)
                self.resolutions_box_layout.addWidget(open_folder_button)
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py

				# Download/Use buttons
				clear_layout(self.resolutions_box_layout)
				hdri.get_resolutions_dowloaded()
				resolutions_available = hdri.get_resolutions_available()
				for r in sorted(resolutions_available.keys()):
					if r in hdri.resolutions_downloaded:
						btn = ResolutionIcon(r,self.main_window,True,None)
					else:
						btn = ResolutionIcon(r,self.main_window,False,resolutions_available[r])
					self.resolutions_box_layout.addWidget(btn,0,Qt.AlignLeft)
				self.resolutions_box_layout.addStretch()
				# Open folder button
				if hdri.local:
					open_folder_button = FolderIcon(self.main_window)
					self.resolutions_box_layout.addWidget(open_folder_button)

# The button which is appended into Light UI inside Gaffer
class BrowseButton(GafferUI.Button):
    def __init__(self, node, **kw):
        GafferUI.Button.__init__(self, "Browse HDRIs", **kw)
        self.__node = node
        self.clickedSignal().connect(Gaffer.WeakMethod(self.clicked), scoped=False)

    def clicked(self, button):
        library = Library()
        window = MainWindow(library, self.__node)
        window.show()


class FolderIcon(QPushButton):
    def __init__(self, mainWindow):
        super(FolderIcon, self).__init__()
        self.mainWindow = mainWindow
        self.selected_hdri = mainWindow.selected

        self.setStyleSheet(
            "background-color:rgb(110,70,10);font: bold 16px;color: white"
        )
        self.setFixedSize(80, 40)
        self.setIcon(pixmap_gaffer_icon("pathChooser.png"))
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        open_file(
            os.path.join(self.mainWindow.lib.local_hdris_path, self.selected_hdri.id)
        )


class ResolutionIcon(QPushButton):
<<<<<<< Updated upstream:python/GafferHaven/gui.py
		def __init__(self,res,mainWindow,downloaded,dowloadLink):
				super(ResolutionIcon, self).__init__()
				self.asset = mainWindow.selected
				self.res = res
				self.downloaded = downloaded
				self.dowloadLink = dowloadLink
				self.main_window = mainWindow
				self.setText(res)
				if downloaded:
					self.setStyleSheet("background-color:rgb(60,90,10);font: bold 16px;color: white");
				else:
					self.setStyleSheet("background-color:rgb(25,25,25);font: bold 16px;color: white");
				self.setFixedSize(80, 40)
				self.clicked.connect(self.on_clicked)
				
		def on_clicked(self):
			if self.downloaded:
				self.asset.use(self.res,self.main_window.origin_node)
			else:
				self.asset.download_and_use(self.res,self.main_window.origin_node,self.dowloadLink)
				self.main_window.info_box.refresh()
				#self.main_window.close()

class FolderIcon(QPushButton):
		def __init__(self,mainWindow):
				super(FolderIcon, self).__init__()
				self.mainWindow = mainWindow
				self.asset = mainWindow.selected
				#self.setText(">")
				self.setStyleSheet("background-color:rgb(110,70,10);font: bold 16px;color: white");
				self.setFixedSize(80, 40)
				self.setIcon(pixmap_gaffer_icon("pathChooser.png"))
				self.clicked.connect(self.on_clicked)
				
		def on_clicked(self):
			open_file( os.path.join(self.mainWindow.lib.local_hdris_path,self.asset.id) )

# The button which is appended into Light UI inside Gaffer
class BrowseButton( GafferUI.Button ):
	def __init__( self, node, **kw ):

		GafferUI.Button.__init__( self, "Browse HDRIs", **kw )
		self.__node = node
		self.clickedSignal().connect( Gaffer.WeakMethod( self.clicked ), scoped = False )

	def clicked( self, button ):
		l = Library()
		mw = MainWindow( l, self.__node)
		mw.show()

# == Utils ==

# Removes all items in layout
def clear_layout(my_layout):
	index = my_layout.count()-1
	while(index >= 0):
		myWidget = my_layout.itemAt(index).widget()
		if (myWidget != None):
			myWidget.setParent(None)
		else:
			my_layout.removeItem(my_layout.itemAt(index))
		index -=1

# creates QPixmap from url on an image
def pixmap_from_URL(url):
	data = urllib.request.urlopen(url).read()
	pixmap = QPixmap()
	pixmap.loadFromData(data)
	return pixmap

# creates QPixmap from icon inside the Gaffer's graphics folder
def pixmap_gaffer_icon(name):
	path = os.environ.get("GAFFER_ROOT")+"/graphics/"+name
	return QPixmap(path)

# Opens the file/folder in OS's file borwser
def open_file(path):
	if platform.system() == "Windows":
		os.startfile(path)
	elif platform.system() == "Darwin":
		subprocess.Popen(["open", path])
	else:
		subprocess.Popen(["xdg-open", path])
=======
    def __init__(self, hdri_resolution, mainWindow, downloaded, dowloadLink):
        super(ResolutionIcon, self).__init__()
        self.selected_hdri = mainWindow.selected
        self.hdri_resolution = hdri_resolution
        self.downloaded = downloaded
        self.dowloadLink = dowloadLink
        self.main_window = mainWindow
        self.setText(hdri_resolution)
        if downloaded:
            self.setStyleSheet(
                "background-color:rgb(60,90,10);font: bold 16px;color: white"
            )
        else:
            self.setStyleSheet(
                "background-color:rgb(25,25,25);font: bold 16px;color: white"
            )
        self.setFixedSize(80, 40)
        self.clicked.connect(self.on_clicked)

    def on_clicked(self):
        if self.downloaded:
            self.selected_hdri.use(self.hdri_resolution, self.main_window.node)
        else:
            self.selected_hdri.download_and_use(
                self.hdri_resolution, self.main_window.node, self.dowloadLink
            )
            self.main_window.info_box.refresh()


if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    app.show()
>>>>>>> Stashed changes:python/GafferHaven/guiTest.py
