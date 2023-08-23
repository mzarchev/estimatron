from nicegui import ui, events
import lib.selected_vars_handler

selected_vars_handler = lib.selected_vars_handler.SelectedVarsHandler()

### UI design

with ui.header().classes("h-12 bg-grey"):
    ui.label("Estimatron")

with ui.row():
    with ui.card():
        ui.upload(on_upload=selected_vars_handler.generate_selects,
                  auto_upload=True,
                  max_files=1,
                  max_file_size=50_000_000, # 50 megabytes max file size
                  label= "Upload a CSV file") \
        .props("accept=.csv")
    with ui.card():
        ui.label("I'm here")

def change_x(event) -> None:
    x = event.value
    print(x)


ui.select(options = [1, 2, 3],
          multiple=True,
          on_change=lambda e: change_x(e)).props("use-chips")
ui.button(text="test",
          on_click=lambda: print(selected_vars_handler.conf))

ui.run()