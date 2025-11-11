from PIL import Image

# Open the uploaded image
input_path = "../../static/textures/Flag2.png"
output_path = "/static/textures/LPrideFlag2.jpg"

# Resize and save
with Image.open(input_path) as img:
    resized_img = img.resize((1024, 1024))
    resized_img = resized_img.convert("RGB")
    resized_img.save(output_path, "JPEG", quality=95)

output_path