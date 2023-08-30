from nicegui import ui

class SelectedVarsHandler:
    def __init__(self):
        self.outc: str = None
        self.pred: str = None
        self.conf = []
        self.specified = False
    
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
        
        # Indicates both pred and outcome have been correctly specified    
        if self.outc and self.pred and self.pred != self.outc:
            self.specified = True 
        else:
            self.specified = False
    
    def generate_selects(self, vars: list) -> None:
        """ 
        Takes a list of variable names as input
        Generates three selection fields
        """
        with ui.column():
            ui.select(
                label="Select outcome variable",
                value="",
                with_input=True,                  
                options=vars,
                on_change=lambda e: self.assign_value(value=e.value,
                                                      var="outc")
                ) \
                    .classes("w-80") 
            ui.select(
                label="Select predictor variable",
                value="",
                options=vars,
                with_input=True,
                on_change=lambda e: self.assign_value(value=e.value,    
                                                      var="pred")
                ) \
                    .classes("w-80") 
            ui.select(
                label="Select confounder variables",
                value="",
                options=vars,
                multiple=True,
                on_change=lambda e: self.assign_value(value=e.value,    
                                                      var="conf")
                ) \
                    .classes("w-80").props("use-chips")
