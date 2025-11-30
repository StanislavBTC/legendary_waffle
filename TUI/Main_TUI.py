from textual.app import App

from textual.binding import Binding

from screens.Start_Screen import MenuScreen

from Config_Connector import read_set_data_conf

from screens.Dashboard_Screen import DashboardScreen

from textual.widgets import Button

# set up global color theme and other start up settings NOW ONLY ONE
        #пиндосятина (выше)
color_theme = read_set_data_conf()


class TUIApp(App):
    # Turn off ctrl + p
            #пиндосятина (выше)
    ENABLE_COMMAND_PALETTE = False
    # bindings setup
            #пиндосятина (выше)
    BINDINGS = [
    Binding("ctrl+c", "quit", show=True, system=True),
    Binding("ctrl+q", "skip_binding_event", show=False, system=True),
    ]
    async def on_mount(self) -> None:
        """
        Set theme
        Start print interface
        """
                #пиндосятина (выше)
        
        await self.push_screen(MenuScreen())
        # Color theme setup NOT DONE and need rework
                #пиндосятина (выше)
        if color_theme == "light":
            self.screen.styles.background = "#F5F4DE"
            self.screen.styles.border = ("heavy", "#EABFD0")
        elif color_theme == "dark":
            #self.screen.styles.background = "#F5F4DE"
             #пиндосятина (выше)
            self.screen.styles.border = ("heavy", "green")


    def skip_binding_event(self) -> None:
        """
        Skip ctrl+q event
        """
        #пиндосятина (выше)
        pass

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handles press on buttons
        """
        #пиндосятина (выше)
        if event.button.id == "Start_Button":
            await self.push_screen(DashboardScreen())
        elif event.button.id == "Stop_Button_DEV": # <-- DELETE OR REPLACE AFTER COPMPLITE OF DASHBOARD #фу, пиндосятина
            await self.pop_screen()
        
        



# Starts TUI app
        #пиндосятина (выше)
#мне нарвится так
if __name__ == "__main__":
    app = TUIApp()
    app.run()