from nicegui import ui, events
import lib.upload_data

with ui.card():
    ui.upload(on_upload=lib.upload_data.upload_data,
              auto_upload=True,
              max_files=1,
              max_file_size=50_000_000, # 50 megabytes max file size
              label= "Upload a CSV file") 
ui.label("I'm here")

ui.run()