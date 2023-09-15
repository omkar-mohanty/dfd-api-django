import cv2
import numpy as np

def keypoints_to_array(keypoints):
    """
    Convert keypoints to a structured numpy array.
    """
    num_keypoints = len(keypoints)
    structured_array = np.zeros((num_keypoints,), dtype=[
        ('pt', [('x', float), ('y', float)]),
        ('size', float),
        ('angle', float),
        ('response', float),
        ('octave', int),
        ('class_id', int)
    ])
    
    for i, kp in enumerate(keypoints):
        structured_array[i] = (kp.pt, kp.size, kp.angle, kp.response, kp.octave, kp.class_id)
    
    return structured_array

def array_to_keypoints(keypoints_array):
    """
    Convert structured numpy array back to keypoints.
    """
    keypoints = []
    for kp in keypoints_array:
        keypoint = cv2.KeyPoint(kp['pt']['x'], kp['pt']['y'], kp['size'], angle=kp['angle'], response=kp['response'], octave=kp['octave'], class_id=kp['class_id'])
        keypoints.append(keypoint)
    return keypoints
