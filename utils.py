from PIL import Image
import numpy as np
import cv2
from io import BytesIO


def load_image(uploaded_file):
    image = Image.open(uploaded_file)
    image = np.array(image)

    if image.shape[-1] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    return image


def convert_image_for_download(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(image_rgb)

    buffer = BytesIO()
    pil_img.save(buffer, format="PNG")

    return buffer.getvalue()