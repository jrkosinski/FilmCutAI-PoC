import base64
import cv2
from io import BytesIO
from PIL import Image

def encode_image_base64(image_path): 
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
        
def encode_frame_base64(frame):
    # Convert color space from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to PIL Image
    pil_img = Image.fromarray(frame)

    # Buffer to store image
    buffer = BytesIO()

    # Save image to buffer
    pil_img.save(buffer, format="JPEG")

    # Base64 encode
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return img_str
    