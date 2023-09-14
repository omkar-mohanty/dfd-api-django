import os
import cv2
import configparser
import numpy as np
from utils.feature_extraction import extract_features
from utils.keypoints_conversion import keypoints_to_array, array_to_keypoints


def store_template(image_path, template_dir):
    """
    Extract features from an image and store them as a template.
    """
    keypoints, descriptors = extract_features(image_path)
    keypoints_list = keypoints_to_array(keypoints)
    
    base_name = os.path.basename(image_path).replace('.png', '')
    np.save(os.path.join(template_dir, f"{base_name}_keypoints.npy"), keypoints_list)
    np.save(os.path.join(template_dir, f"{base_name}_descriptors.npy"), descriptors)


def match_template(image_path, template_dir):
    """
    Match an image against stored templates.
    """
    # Extract features from the given image
    keypoints1, descriptors1 = extract_features(image_path)
    
    # BFMatcher (Brute Force Matcher) with default params
    bf = cv2.BFMatcher()
    
    for template in os.listdir(template_dir):
        if "_descriptors.npy" in template:
            base_name = template.replace('_descriptors.npy', '')
            keypoints_list = np.load(os.path.join(template_dir, f"{base_name}_keypoints.npy"))
            keypoints2 = array_to_keypoints(keypoints_list)
            descriptors2 = np.load(os.path.join(template_dir, template))
            
            # Match descriptors
            matches = bf.knnMatch(descriptors1, descriptors2, k=2)
            
            # Apply ratio test
            good_matches = [m for m, n in matches if m.distance < RATIO_TEST * n.distance]
            
            # If a significant number of good matches are found, it's likely a match
            if len(good_matches) > MATCH_THRESHOLD:
                print(f"Image matches with template: {base_name}")
                return True
    print("No matching template found.")
    return False


config = configparser.ConfigParser()
config.read('config.ini')
MATCH_THRESHOLD = int(config['DEFAULT']['MATCH_THRESHOLD'])
RATIO_TEST = float(config['DEFAULT']['RATIO_TEST'])