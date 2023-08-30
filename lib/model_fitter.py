import statsmodels.formula.api as smf 

class modelFitter:
    def __init__(self):
        self.formula: str = None
        self.summary = None,
    
    def format_formula(self, pred: str, outc: str, conf=[]):
        # Take a predictor, an outcome and optionally a list of confounders
        # Return a formatted formula string
        formula = f"{outc} ~ {pred}"
        if conf: formula = f"{formula} + {' + '.join(conf)}"
        self.formula = formula
        
    def fit_model(self, formula, df):
        fit = smf.logit(formula, data=df).fit()
        self.summary = fit.summary()
        #me.avg_comparisons(fit_sm, variables={"x": [0, 1]})