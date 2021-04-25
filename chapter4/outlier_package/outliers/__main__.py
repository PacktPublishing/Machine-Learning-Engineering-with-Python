from utils.data import create_data
from detectors.detection_models import DetectionModels
import detectors._base

import os
dirname = os.path.dirname(__file__)
MODEL_CONFIG_PATH = os.path.join(dirname, "configs/model_config.json")
#MODEL_CONFIG_PATH = "./configs/model_config.json"

if __name__ == "__main__":
    data = create_data()
    models = DetectionModels(MODEL_CONFIG_PATH).get_models()
    for model in models:
        detector = detectors._base.OutlierDetector(model=model)
        result = detector.detect(data)
        print(result)
