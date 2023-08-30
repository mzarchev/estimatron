from nicegui import ui, events
import lib.selected_vars_handler
import lib.csv_file_handler


selected_vars_handler = lib.selected_vars_handler.SelectedVarsHandler()
csv_file_handler = lib.csv_file_handler.CsvFileHandler()


# Functions
def respond_to_upload(event: events.UploadEventArguments):
    csv_file_handler.upload_csv(event)
    selected_vars_handler.generate_selects(csv_file_handler.cols)
 
### UI design
with ui.header().classes("h-12 bg-grey"):
    ui.label("Estimatron")

with ui.row():
    with ui.card():
        ui.upload(on_upload=respond_to_upload,
                  auto_upload=True,
                  max_files=1,
                  max_file_size=50_000_000, # 50 megabytes max file size
                  label= "Upload a CSV file") \
        .props("accept=.csv")
    
    with ui.card():
        ui.button(text="Fit model",
                  on_click=lambda: print("clicked")) \
        .bind_enabled(selected_vars_handler, "specified")

def change_x(event) -> None:
    x = event.value
    print(x)


ui.select(options = [1, 2, 3],
          multiple=True,
          on_change=lambda e: change_x(e)).props("use-chips")
ui.button(text="test",
          on_click=lambda: print(f"{selected_vars_handler.outc} --- {selected_vars_handler.pred}"))

ui.run()