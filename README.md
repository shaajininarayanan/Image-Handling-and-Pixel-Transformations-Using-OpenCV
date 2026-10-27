# Image-Handling-and-Pixel-Transformations-Using-OpenCV

## AIM:
Write a Python program using OpenCV that performs the following tasks:

- Read and Display an Image.
- Adjust the brightness of an image.
- Modify the image contrast.
- Generate a third image using bitwise operations.

## Software Required:
- Anaconda - Python 3.7
- Jupyter Notebook (for interactive development and execution)

## Algorithm:

**Step 1:**  
Load an image from your local directory and display it.

**Step 2:**  
Create a matrix of ones (with data type float64) to adjust brightness.

**Step 3:**  
Create brighter and darker images by adding and subtracting the matrix from the original image. Display the original, brighter, and darker images.

**Step 4:**  
Modify the image contrast by creating two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix). Display the original, lower contrast, and higher contrast images.

**Step 5:**  
Split the image (`Boy.jpg`) into B, G, R components and display the channels.

## Program Developed By:

**Name:** Shaajini N

**Register Number:** 212225040395

## Ex. No. 01

### 1. Read the image (`Eagle_in_Flight.jpg`) using OpenCV `imread()` as a grayscale image.
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Eagle_in_Flight.jpg", cv2.IMREAD_GRAYSCALE)
```

### 2. Print the image width, height & channel.
```python
height, width = img.shape

print("Width:", width)
print("Height:", height)
print("Channel:", 1)
```

### 3. Display the image using Matplotlib `imshow()`.
```python
plt.imshow(img, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()
```

### 4. Save the image as a PNG file using OpenCV `imwrite()`.
```python
cv2.imwrite("Eagle_Grayscale.png", img)
```

### 5. Read the saved image above as a color image using `cv2.cvtColor()`.
```python
gray_img = cv2.imread("Eagle_Grayscale.png", cv2.IMREAD_GRAYSCALE)
color_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
```

### 6. Display the colour image using Matplotlib `imshow()` and print the image width, height & channel.
```python
height, width, channel = color_img.shape

print("Width:", width)
print("Height:", height)
print("Channel:", channel)

plt.imshow(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
plt.title("Colour Image")
plt.axis("off")
plt.show()
```

### 7. Crop the image to extract any specific object (Eagle alone) from the image.
```python
eagle = cv2.imread("Eagle_in_Flight.jpg")

x, y, w, h = cv2.selectROI("Select Eagle", eagle, False)
cv2.destroyAllWindows()

eagle_crop = eagle[y:y+h, x:x+w]

plt.imshow(cv2.cvtColor(eagle_crop, cv2.COLOR_BGR2RGB))
plt.title("Cropped Eagle")
plt.axis("off")
plt.show()
```

### 8. Resize the image up by a factor of 2x.
```python
eagle_resized = cv2.resize(
    eagle_crop, None, fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR
)

plt.imshow(cv2.cvtColor(eagle_resized, cv2.COLOR_BGR2RGB))
plt.title("Resized Eagle")
plt.axis("off")
plt.show()
```

### 9. Flip the cropped/resized image horizontally.
```python
eagle_flipped = cv2.flip(eagle_resized, 1)

plt.imshow(cv2.cvtColor(eagle_flipped, cv2.COLOR_BGR2RGB))
plt.title("Flipped Eagle")
plt.axis("off")
plt.show()
```

### 10. Read in the image (`Apollo-11-launch.jpg`).
```python
apollo = cv2.imread("Apollo-11-launch.jpg")

plt.imshow(cv2.cvtColor(apollo, cv2.COLOR_BGR2RGB))
plt.title("Apollo 11 Launch")
plt.axis("off")
plt.show()
```

### 11. Add the following text to the dark area at the bottom of the image (centered on the image).
```python
text = 'Apollo 11 Saturn V Launch, July 16, 1969'
font_face = cv2.FONT_HERSHEY_PLAIN
font_scale = 1.5
thickness = 2
height, width = apollo.shape[:2]

text_width = cv2.getTextSize(
    text, font_face, font_scale, thickness
)[0][0]

text_x = (width - text_width) // 2
text_y = height - 20

cv2.putText(
    apollo, text, (text_x, text_y),
    font_face, font_scale, (255, 255, 255),
    thickness, cv2.LINE_AA
)

```

### 12. Draw a magenta rectangle that encompasses the launch tower and the rocket.
```python
rect_color = (255, 0, 255)  # Magenta in BGR format

cv2.rectangle(
    apollo,
    (int(apollo.shape[1] * 0.35), int(apollo.shape[0] * 0.10)),
    (int(apollo.shape[1] * 0.70), int(apollo.shape[0] * 0.85)),
    rect_color,
    3
)

```

### 13. Display the final annotated image.
```python
plt.imshow(cv2.cvtColor(apollo, cv2.COLOR_BGR2RGB))
plt.title("Final Annotated Apollo Image")
plt.axis("off")
plt.show()

cv2.imwrite("Apollo_Annotated.jpg", apollo)
```

### 14. Read the image (`Boy.jpg`).
```python
img = cv2.imread("Boy.jpg")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()
```

### 15. Adjust the brightness of the image. Create a matrix of ones with data type `float64`.
```python
matrix_ones = np.ones(img.shape, dtype=np.float64)
```

### 16. Create brighter and darker images.
```python
matrix = (matrix_ones * 50).astype(np.uint8)

img_brighter = cv2.add(img, matrix)
img_darker = cv2.subtract(img, matrix)
```

### 17. Display the images (Original Image, Darker Image, Brighter Image).
```python
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img_darker, cv2.COLOR_BGR2RGB))
plt.title("Darker Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(img_brighter, cv2.COLOR_BGR2RGB))
plt.title("Brighter Image")
plt.axis("off")

plt.show()
```

### 18. Modify the image contrast. Create two higher contrast images using scaling factors of 1.1 and 1.2 (without overflow fix).
```python
matrix1 = np.ones(img.shape, dtype=np.float64) * 1.1
matrix2 = np.ones(img.shape, dtype=np.float64) * 1.2

img_higher1 = (img.astype(np.float64) * matrix1).astype(np.uint8)
img_higher2 = (img.astype(np.float64) * matrix2).astype(np.uint8)
```

### 19. Display the images (Original, Lower Contrast, Higher Contrast).
```python
img_lower = (img.astype(np.float64) * 0.8).astype(np.uint8)

plt.figure(figsize=(18, 5))

images = [img, img_lower, img_higher1, img_higher2]
titles = [
    "Original Image",
    "Lower Contrast",
    "Higher Contrast 1.1",
    "Higher Contrast 1.2"
]

for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis("off")

plt.show()
```

### 20. Split the image (`Boy.jpg`) into B, G, R components and display the channels.
```python
b, g, r = cv2.split(img)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(b, cmap="gray")
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(g, cmap="gray")
plt.title("Green Channel")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(r, cmap="gray")
plt.title("Red Channel")
plt.axis("off")

plt.show()
```

### 21. Merge the R, G, B channels and display them along with the original image.
```python
merged_img = cv2.merge([b, g, r])

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(merged_img, cv2.COLOR_BGR2RGB))
plt.title("Merged Image")
plt.axis("off")

plt.show()
```

### 22. Split the image into H, S, V components and display the channels.
```python
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(h, cmap="gray")
plt.title("Hue Channel")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(s, cmap="gray")
plt.title("Saturation Channel")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(v, cmap="gray")
plt.title("Value Channel")
plt.axis("off")

plt.show()
```

### 23. Merge the H, S, V channels and display them along with the original image.
```python
hsv_merged = cv2.merge([h, s, v])
merged_bgr = cv2.cvtColor(hsv_merged, cv2.COLOR_HSV2BGR)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(merged_bgr, cv2.COLOR_BGR2RGB))
plt.title("Merged HSV Image")
plt.axis("off")

plt.show()
```
### 24. Generate a third image using bitwise operations.
```python
img1 = cv2.imread("Boy.jpg")
img2 = cv2.imread("Apollo-11-launch.jpg")

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

third_img = cv2.bitwise_and(img1, img2)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("Image 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Image 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(third_img, cv2.COLOR_BGR2RGB))
plt.title("Third Image - Bitwise AND")
plt.axis("off")

plt.show()

cv2.imwrite("Third_Image.jpg", third_img)
```

## Output:

i) Read and Display an Image.
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/e0efdc1f-80dc-472a-8509-eba539075ef8" />

ii) Adjust Image Brightness.
<img width="1917" height="1077" alt="image" src="https://github.com/user-attachments/assets/b496df40-7bed-4623-9c3d-2c83861c0a44" />

iii) Modify Image Contrast.
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/10b87650-98a8-4162-87eb-e1824b542b54" />

iv) Generate Third Image Using Bitwise Operations.
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/7d15612c-b682-4871-8f57-374645150aa6" />

## Result:

Thus, the images were read, displayed, brightness and contrast adjustments were made, and bitwise operations were performed successfully using the Python program.
