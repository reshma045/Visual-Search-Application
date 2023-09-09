from PIL import Image
from main_feature import FeatureExtractor
from pathlib import Path
import numpy as np

if __name__ == '__main__':
    fe = FeatureExtractor()

    for img_path in sorted(Path("./static/img").glob("*.png")):
        print(img_path)  
        feature = fe.extract(img=Image.open(img_path))
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")  
        np.save(feature_path, feature)
