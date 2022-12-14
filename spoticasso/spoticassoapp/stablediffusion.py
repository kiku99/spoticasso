import replicate
import urllib.request
from PIL import Image

def download_image(keywords: list) -> None:
    url = generate_image_url(keywords)
    file_name = "_".join(" ".join(keywords).split()) + ".jpeg"
    save_location = "/Users/kiku/Desktop/spoticasso/images/"
    urllib.request.urlretrieve(url, save_location + file_name)
    image = Image.open(save_location + file_name)
    new_image = image.resize((256, 256))
    new_image.save(save_location + file_name)

    return file_name

def generate_image_url(keywords: list) -> str:
    prompt = ", ".join(keywords)
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")
    img_url = version.predict(prompt=prompt)[0]
    return img_url


