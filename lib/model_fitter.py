import statsmodels.formula.api as smf 
from pandas import read_csv
import marginaleffects as me

class modelFitter:
    def __init__(self):
        self.formula: str = None
        self.pred: str    = None
        self.summary      = None
        self.fit          = None
        self.ate          = None
    
    def format_formula(self, pred: str, outc: str, conf=[]):
        # Take a predictor, an outcome and optionally a list of confounders
        # Return a formatted formula string
        formula = f"{outc} ~ {pred}"
        if conf: formula = f"{formula} + {' + '.join(conf)}"
        self.pred = pred
        self.formula = formula
        
    def fit_model(self, formula, df):
        fit = smf.ols(formula, data=df).fit()
        self.fit = fit
        self.summary = fit.summary()
        
    def estimate_ate(self, fit, pred):
        df_ate = me.avg_comparisons(fit, variables=pred)
        ate = df_ate.get_column("estimate")[0]
        ci_low = df_ate.get_column("conf_low")[0]
        ci_upp = df_ate.get_column("conf_high")[0]
        p = df_ate.get_column("p_value")[0]
        
        ate_fmt = f"{round(ate, 2)} [{round(ci_low, 2)}, {round(ci_upp, 2)}], p={round(p, 3)}"
        self.ate = ate_fmt
        
    def run_fitting(self, pred, outc, data, conf=[]):
        self.format_formula(pred, outc, conf)
        self.fit_model(self.formula, data)
        self.estimate_ate(self.fit, pred)


""" model = modelFitter()

df_lbd = read_csv("../df_lbd.csv")

formula = model.format_formula()
model.run_fitting(pred="Year", outc="Runtime",
                  data=df_lbd)

model.ate """