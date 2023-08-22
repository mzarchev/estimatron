from nicegui import ui, events
from io import StringIO
import pandas as pd

class csvFile:
    def __init__(self):
        self.df = None
        self.cols = []
    
    def upload_csv(self, event: events.UploadEventArguments):
        with StringIO(event.content.read().decode()) as f:
            self.df = pd.read_csv(f)   
            self.cols = self.df.columns.to_list()

def handle_upload(event: events.UploadEventArguments) -> None:
    csv_file = csvFile()
    csv_file.upload_csv(event)
    
    with ui.column():
        ui.button("Print first column", 
                  on_click=lambda: print(csv_file.cols))            

up = ui.upload(on_upload=handle_upload,
               auto_upload=True,
               max_files=1,
               max_file_size=50_000_000, # 50 megabytes max file size
                label= "Upload a CSV file"
               ) 

ui.run()