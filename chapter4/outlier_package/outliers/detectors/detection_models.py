import json
from sklearn.ensemble import IsolationForest

class DetectionModels(object):
    def __init__(self, model_config_path=None):
        if model_config_path is not None:
            with open(model_config_path) as w:
                self.model_def = json.load(w)
    def forest_model(self):
        return self.model_def