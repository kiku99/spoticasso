import replicate
import webbrowser

# a = replicate.Client(api_token="fbb40159d93c03b9be3175f23643fbf70f3ed1d5")
# # model = a.models.get("stability-ai/stable-diffusion")
# # model.predict("a 19th century portrait of a wombat gentleman")

# a.models.get("stability-ai/stable-diffusion")
# print(a)
# replicate.models.
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("8abccf52e7cba9f6e82317253f4a3549082e966db5584e92c808ece132037776")
output = version.predict(prompt="nananana, nanana, feelings")[0]

print(output)
webbrowser.open(output)