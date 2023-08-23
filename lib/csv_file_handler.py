from io import StringIO
from nicegui import events
import pandas as pd


class CsvFileHandler:
    def __init__(self):
        self.df = None
        self.cols = []
    
    def upload_csv(self, event: events.UploadEventArguments):
        with StringIO(event.content.read().decode()) as f:
            self.df = pd.read_csv(f)   
            self.cols = self.df.columns.to_list()

