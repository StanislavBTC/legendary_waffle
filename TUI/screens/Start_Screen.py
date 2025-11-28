from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Checkbox, ListView, ListItem, Label
from textual.containers import Horizontal, Vertical
from textual.containers import Container
from Config_Connector import read_set_data_conf

# set up local color theme and other start up settings NOW ONLY ONE
color_theme = read_set_data_conf()


class MenuScreen(Screen):
    # CSS colortheme setup (NOW IN DEV NEED FIX)
    if color_theme == "light":
        CSS = """
        Screen {
            align: center middle;
        }
        ListView {
            background: #EABFD0;
            width: 60;
            height: auto;
            margin: 2 2;
        }
        Label {
            color: black;
            padding: 1 1;
        }
        Button {
            margin: 2 2;
            padding: 1 1;
        }
        Checkbox {
            background: #EABFD0;
            color: black;
            margin: 2 20;
            padding: 1 1;
        }
        """
    elif color_theme == "dark":
        CSS = """
        Screen {
            align: center middle;
        }
        #traffic_source_list_container {
            border: dashed green;
            width: auto;
            height: auto;
            padding: 1 2;
        }
        ListView {
            scrollbar-visibility: visible;
            scrollbar-color: green;
            scrollbar-color-hover: darkgreen;
            scrollbar-color-active: forestgreen;
            width: 45;
            height: 25;
        }
        Label {
            padding: 1 1;
        }
        Button {
            align: center middle;
            padding: 1 1;
            margin: 2 4;
        }
        Checkbox {
            align: center middle;    
            padding: 1 1;
        }
        #checkbox_container {
            align: center middle; 
            border: dashed green;
            width: 25;
            height: 10;
        }
        """
    def compose(self) -> ComposeResult:
        """
        Display interface
        """
        with Horizontal():
            traffic_source_list_container = Container(  ListView(
                ListItem(Label("eno\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("wfi\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
                ListItem(Label("blt\nAddresses:fe80::c2b:c0f2:62e5:c757\n192.168.1.103")),
            ),id="traffic_source_list_container")
            traffic_source_list_container.border_title = "Traffic sources:"
            yield traffic_source_list_container
            checkbox_container = Container(
                Checkbox("Option 1:", compact= True),
                Checkbox("Option 2:", compact= True), 
                id="checkbox_container")
            checkbox_container.border_title = "Options:"
            with Vertical():
                yield checkbox_container
                yield Button("Start",variant="success", compact= True, id="Start_Button")


