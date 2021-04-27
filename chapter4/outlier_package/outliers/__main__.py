from utils.data import create_data
from detectors.detection_models import DetectionModels
import detectors.pipelines
from definitions import MODEL_CONFIG_PATH


if __name__ == "__main__":
    data = create_data()
    models = DetectionModels(MODEL_CONFIG_PATH).get_models()
    for model in models:
        detector = detectors.pipelines.OutlierDetector(model=model)
        result = detector.detect(data)
        print(result)
