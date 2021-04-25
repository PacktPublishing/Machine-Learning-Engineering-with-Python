from sklearn.ensemble import IsolationForest
from utils.data import create_data
import detectors._base

MODEL_CONFIG_PATH = "configs/model_config.json"

if __name__ == "__main__":
    data = create_data()

    detector = detectors._base.OutlierDetector(model=model)

    result = detector.detect(data)
