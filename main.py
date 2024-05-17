from openai import OpenAI
import requests
from  hook_key_board_exception import hook_keyboard_excetion_hw
hook_keyboard_excetion_hw()


def generate_image(prompt):
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )

    image_url = response.data[0].url
    try:
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open("output.jpeg", "wb") as file:
                file.write(image_response.content)
        else:
            pass
    except Exception as e:
        pass


   
while True:
    prompt = input(">> ")
    generate_image(prompt)


# 帮我生成一张小朋友的照片，并生成为骑士服