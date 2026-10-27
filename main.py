
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def read_image(filename, grayscale=False):
    path = IMAGE_DIR / filename
    mode = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    image = cv2.imread(str(path), mode)

    if image is None:
        raise FileNotFoundError(f"Image not found: {path}")

    return image


def display_images(images, titles, gray=False):
    plt.figure(figsize=(15, 5))

    for i, (image, title) in enumerate(zip(images, titles), 1):
        plt.subplot(1, len(images), i)

        if image.ndim == 2:
            plt.imshow(image, cmap="gray")
        else:
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


# 1. Read Eagle image as grayscale
eagle_gray = read_image("Eagle_in_Flight.jpg", grayscale=True)
height, width = eagle_gray.shape

print("Eagle Grayscale Image")
print("Width:", width)
print("Height:", height)
print("Channels: 1")

display_images([eagle_gray], ["Eagle - Grayscale"])
cv2.imwrite(str(OUTPUT_DIR / "eagle_gray.png"), eagle_gray)

# 2. Convert grayscale to 3-channel BGR image
eagle_color = cv2.cvtColor(eagle_gray, cv2.COLOR_GRAY2BGR)
h, w, channels = eagle_color.shape

print("\nConverted Image")
print("Width:", w, "Height:", h, "Channels:", channels)

display_images([eagle_color], ["Eagle - Converted Image"])

# 3. Crop, resize and flip
# Adjust coordinates if needed to isolate the eagle.
eagle_crop = eagle_color.copy()

eagle_resized = cv2.resize(
    eagle_crop, None, fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR
)
eagle_flipped = cv2.flip(eagle_resized, 1)

cv2.imwrite(str(OUTPUT_DIR / "eagle_crop.png"), eagle_crop)
cv2.imwrite(str(OUTPUT_DIR / "eagle_resized.png"), eagle_resized)
cv2.imwrite(str(OUTPUT_DIR / "eagle_flipped.png"), eagle_flipped)

display_images(
    [eagle_crop, eagle_resized, eagle_flipped],
    ["Eagle Crop", "Resized 2x", "Horizontal Flip"]
)

# 4. Read Apollo launch image and annotate
apollo = read_image("Apollo-11-launch.jpg")
annotated = apollo.copy()
ah, aw = annotated.shape[:2]

caption = "Apollo 11 Saturn V Launch, July 16, 1969"
font = cv2.FONT_HERSHEY_PLAIN
scale = 1.5
thickness = 2

(text_width, text_height), _ = cv2.getTextSize(
    caption, font, scale, thickness
)

text_x = max(0, (aw - text_width) // 2)
text_y = max(text_height + 5, ah - 15)

cv2.putText(
    annotated, caption, (text_x, text_y), font,
    scale, (255, 255, 255), thickness, cv2.LINE_AA
)

# Magenta rectangle: BGR format
# Approximate coordinates; adjust for your Apollo image.
cv2.rectangle(
    annotated,
    (int(aw * 0.25), int(ah * 0.10)),
    (int(aw * 0.75), int(ah * 0.85)),
    (255, 0, 255), 3
)

cv2.imwrite(str(OUTPUT_DIR / "apollo_annotated.jpg"), annotated)
display_images([apollo, annotated], ["Apollo Original", "Apollo Annotated"])

# 5. Read Boy image
img = read_image("Boy.jpg")
display_images([img], ["Original Boy Image"])

# 6. Brightness adjustment
matrix_ones = np.ones(img.shape, dtype=np.float64)
img_float = img.astype(np.float64)

# Add/subtract brightness value
img_brighter = cv2.add(img_float, matrix_ones * 40)
img_darker = cv2.subtract(img_float, matrix_ones * 40)

img_brighter = np.clip(img_brighter, 0, 255).astype(np.uint8)
img_darker = np.clip(img_darker, 0, 255).astype(np.uint8)

cv2.imwrite(str(OUTPUT_DIR / "boy_brighter.jpg"), img_brighter)
cv2.imwrite(str(OUTPUT_DIR / "boy_darker.jpg"), img_darker)

display_images(
    [img, img_darker, img_brighter],
    ["Original", "Darker", "Brighter"]
)

# 7. Contrast adjustment
matrix_low = np.ones(img.shape, dtype=np.float64) * 0.8
matrix1 = np.ones(img.shape, dtype=np.float64) * 1.1
matrix2 = np.ones(img.shape, dtype=np.float64) * 1.2

img_lower = cv2.multiply(img_float, matrix_low)
img_higher1 = cv2.multiply(img_float, matrix1)
img_higher2 = cv2.multiply(img_float, matrix2)

img_lower = np.clip(img_lower, 0, 255).astype(np.uint8)
img_higher1 = np.clip(img_higher1, 0, 255).astype(np.uint8)
img_higher2 = np.clip(img_higher2, 0, 255).astype(np.uint8)

display_images(
    [img, img_lower, img_higher1],
    ["Original", "Lower Contrast", "Higher Contrast 1.1"]
)
display_images([img, img_higher2], ["Original", "Higher Contrast 1.2"])

cv2.imwrite(str(OUTPUT_DIR / "boy_lower_contrast.jpg"), img_lower)
cv2.imwrite(str(OUTPUT_DIR / "boy_contrast_1_1.jpg"), img_higher1)
cv2.imwrite(str(OUTPUT_DIR / "boy_contrast_1_2.jpg"), img_higher2)

# 8. Split B, G, R channels
B, G, R = cv2.split(img)

display_images([B, G, R], ["Blue Channel", "Green Channel", "Red Channel"])

# Merge RGB channels and display
rgb_merged = cv2.merge([R, G, B])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(rgb_merged)
plt.title("Merged RGB Image")
plt.axis("off")
plt.tight_layout()
plt.show()

cv2.imwrite(str(OUTPUT_DIR / "boy_rgb_merged.png"),
            cv2.cvtColor(rgb_merged, cv2.COLOR_RGB2BGR))

# 9. Split H, S, V channels
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv)

display_images([H, S, V], ["Hue Channel", "Saturation Channel",
                            "Value Channel"])

# Merge HSV channels and convert back to BGR for display
hsv_merged = cv2.merge([H, S, V])
bgr_merged = cv2.cvtColor(hsv_merged, cv2.COLOR_HSV2BGR)

display_images([img, bgr_merged],
               ["Original Image", "Merged HSV Image"])

cv2.imwrite(str(OUTPUT_DIR / "boy_hsv_merged.png"), bgr_merged)

# 10. Bitwise operation using a circular mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)
center = (img.shape[1] // 2, img.shape[0] // 2)
radius = min(img.shape[:2]) // 4

cv2.circle(mask, center, radius, 255, -1)

bitwise_result = cv2.bitwise_and(img, img, mask=mask)

cv2.imwrite(str(OUTPUT_DIR / "boy_mask.png"), mask)
cv2.imwrite(str(OUTPUT_DIR / "boy_bitwise_and.png"), bitwise_result)

display_images(
    [img, bitwise_result],
    ["Original Image", "Bitwise AND Result"]
)

print("\nAll OpenCV experiment steps completed successfully!")
print("Check the outputs folder for saved images.")
