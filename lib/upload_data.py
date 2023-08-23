from nicegui import events, ui
import lib.csv_file

def upload_data(event: events.UploadEventArguments) -> None:
    csv_file = lib.csv_file.csvFile()
    csv_file.upload_csv(event)
    
    with ui.column():
        ui.select(label="Select outcome variable",
                  with_input=True,                  
                  options=csv_file.cols,
                  value=csv_file.cols[1]) \
                      .classes("w-80")
        ui.select(label="Select predictor variable",
                  options=csv_file.cols,
                  with_input=True,
                  value=csv_file.cols[2]) \
                      .classes("w-80")
        ui.select(label="Select confounder variables",
                  options=csv_file.cols,
                  multiple=True,
                  value=csv_file.cols[3]) \
                      .classes("w-80").props("use-chips")
