import replicate
import urllib.request


def download_image(keywords: list) -> None:
    url = generate_image(keywords)
    file_name = "_".join(keywords) + ".png"
    save_location = "./images/"
    urllib.request.urlretrieve(url, save_location + file_name)


def generate_image(keywords: list) -> str:
    prompt = ", ".join(keywords)
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")
    img_url = version.predict(prompt=prompt)[0]
    return img_url


if __name__ == "__main__":
    keywords = ['she', 'night', 'raise']
    download_image(keywords)
