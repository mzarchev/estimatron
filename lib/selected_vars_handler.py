from nicegui import events, ui
import lib.csv_file_handler

csv_file_handler = lib.csv_file_handler.CsvFileHandler()

class SelectedVarsHandler:
    def __init__(self):
        self.outc = ""
        self.pred = ""
        self.conf = []
    
    def assign_value(self, value:str | list, var:str) -> None:
        """ 
        Assigns values to outcome, predictor and confounders variables for easy access
        """
        if var == "outc":
            self.outc = value
        elif var == "pred":
            self.pred = value
        elif var == "conf":
            self.conf = value
    
    
    def generate_selects(self, event: events.UploadEventArguments) -> None:
        """ 
        Passes the event from the upload selector to the csv handler
        Generates selection fields based on the columns of the csv file
        """
        csv_file_handler.upload_csv(event)
        
        with ui.column():
            ui.select(
                label="Select outcome variable",
                value="Outcome",
                with_input=True,                  
                options=csv_file_handler.cols,
                on_change=lambda e: self.assign_value(value=e.value,
                                                      var="outc")
                ) \
                    .classes("w-80") 
            ui.select(
                label="Select predictor variable",
                value="Predictor",
                options=csv_file_handler.cols,
                with_input=True,
                on_change=lambda e: self.assign_value(value=e.value,    
                                                      var="pred")
                ) \
                    .classes("w-80") 
            ui.select(
                label="Select confounder variables",
                value="Confounders",
                options=csv_file_handler.cols,
                multiple=True,
                on_change=lambda e: self.assign_value(value=e.value,    
                                                      var="conf")
                ) \
                    .classes("w-80").props("use-chips")
