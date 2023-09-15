import cv2

def extract_features(image_path):
    """
    Extract features from an image using ORB (Oriented FAST and Rotated BRIEF) detector.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(image, None)
    
    # Just for testing
    # Draw keypoints on the image
    # image_with_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # # Display the image with keypoints in a resizable window
    # cv2.namedWindow("Keypoints", cv2.WINDOW_NORMAL)
    # cv2.imshow("Keypoints", image_with_keypoints)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return keypoints, descriptors
