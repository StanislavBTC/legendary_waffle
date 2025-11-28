from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Checkbox, ListView, ListItem, Label
from textual.containers import Horizontal, Vertical
from textual_plotext import PlotextPlot
from textual.containers import Container
import asyncio




class SpeedInternetStreamingDataPlot(PlotextPlot):
    """Class of upadating upload-download speed of internet"""

    def __init__(self, max_length=300):  # Max length of plot before update
        super().__init__()
        self.max_length = max_length

    async def on_mount(self) -> None:
        """Setup settings of plot"""
        self.plt.title("Traffic rate")
        self.set_interval(0.25, self.plot)
        self.download_speed_data = []
        self.upload_speed_data = []
        
        asyncio.create_task(self.update_speed_data_loop())

    async def update_speed_data(self, new_download_speed_data_num: float, new_upload_speed_data_num: float) -> None:
        """Add new speed data and update speed data from old to new when max lenght reached"""
        if len(self.download_speed_data) >= self.max_length:
            self.download_speed_data.pop(0)
        if len(self.upload_speed_data) >= self.max_length:
            self.upload_speed_data.pop(0)
        self.download_speed_data.append(new_download_speed_data_num)
        self.upload_speed_data.append(new_upload_speed_data_num)

    async def plot(self) -> None:
        """Setup plots"""
        self.plt.clear_data()
        if self.download_speed_data:
            self.plt.scatter(self.download_speed_data, marker='dot', label='Download')
        if self.upload_speed_data:
            self.plt.scatter(self.upload_speed_data, marker='dot', label='Upload')
        self.plt.xticks([])
        self.plt.ylabel("Speed in MB/S")
        #self.plt.yticks(range(0, 101))  # Set int numbers on Y
        self.refresh()
        
    async def update_speed_data_loop(self):
        """Loop of update of speed data"""
        while True:
            new_download_speed_data_num = 1 #<- FIXED DATA UPDATE
            new_upload_speed_data_num = 0 #<- FIXED DATA UPDATE
            await self.update_speed_data(new_download_speed_data_num, new_upload_speed_data_num)
            await asyncio.sleep(0.1)  # Speed of update plot

class DashboardScreen(Screen):
    CSS = """
        Screen {
            align: center middle;
        }
        ListView {
            width: 60;
            height: auto;
            margin: 2 2;
        }
        Label {
            padding: 1 1;
        }
        Button {
            margin: 2 20;
            padding: 1 1;
        }
        Checkbox {
            margin: 2 20;
            padding: 1 1;
        }
        """
    def compose(self) -> ComposeResult:
        """
        Display interface 
        """
        speed_plot_container = Container(
                SpeedInternetStreamingDataPlot(),
                id="speed_plot_container")
        speed_plot_container.border_title = "Plot:"
        with Horizontal():
            with Vertical():
                yield Label("1")
                yield Label("2")
            with Vertical():
                yield speed_plot_container
                yield Label("3")
            
        yield Button("STOP-DEV-BUTTON",variant="success", compact= True, id="Stop_Button_DEV")