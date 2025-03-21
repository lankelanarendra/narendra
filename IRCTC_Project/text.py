import cv2
import os
import numpy as np

# Define file paths (use full paths if needed)
virat_path = "virat.jpg"
rohit_path = "rohit.jpg"

# Check if files exist before loading
if not os.path.exists(virat_path) or not os.path.exists(rohit_path):
    print("Error: One or both image files not found. Please check file paths.")
else:
    # Load images
    virat_img = cv2.imread(virat_path)
    rohit_img = cv2.imread(rohit_path)

    # Resize both images to the same height
    height = 500  # Adjust as needed
    virat_img = cv2.resize(virat_img, (int(virat_img.shape[1] * height / virat_img.shape[0]), height))
    rohit_img = cv2.resize(rohit_img, (int(rohit_img.shape[1] * height / rohit_img.shape[0]), height))

    # Ensure both images have the same width
    min_width = min(virat_img.shape[1], rohit_img.shape[1])
    virat_img = cv2.resize(virat_img, (min_width, height))
    rohit_img = cv2.resize(rohit_img, (min_width, height))

    # Concatenate images
    combined_image = np.hstack((virat_img, rohit_img))

    # Save and display the final image
    cv2.imwrite("combined_image.jpg", combined_image)
    cv2.imshow("Virat Kohli & Rohit Sharma", combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
