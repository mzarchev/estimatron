from nicegui import ui, events
import lib.selected_vars_handler
import lib.csv_file_handler
import lib.model_fitter

selected_vars_handler = lib.selected_vars_handler.SelectedVarsHandler()
csv_file_handler = lib.csv_file_handler.CsvFileHandler()
model_fitter = lib.model_fitter.modelFitter()

# Functions
def respond_to_upload(event: events.UploadEventArguments):
    csv_file_handler.upload_csv(event)
    selected_vars_handler.generate_selects(csv_file_handler.cols)
 
def respond_to_fit_model():
    model_fitter.run_fitting(pred=selected_vars_handler.pred,
                             outc=selected_vars_handler.outc,
                             conf=selected_vars_handler.conf,
                             data=csv_file_handler.df) 
 
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
                  on_click=respond_to_fit_model) \
        .bind_enabled(selected_vars_handler, "specified")
        
        ui.label() \
        .bind_text(model_fitter, "ate") \
        .bind_visibility(model_fitter, "ate")
        
        ui.label()

ui.run()