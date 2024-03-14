import base64
import anthropic

from Extraction_FinalCode import convert_any_to_string

client = anthropic.Anthropic(
    api_key= "your-api-key"
)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_image

# ... (existing code)

def main():
    global text, encoded_image
    global data_string
    filepath = "MLOps.jpg"
    new_path = filepath.lower()

    try:
        text = convert_any_to_string(new_path)
        encoded_image = encode_image(new_path)
    except Exception as e:
        print("Error: ", e)

    data_string = text

    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1001,
        temperature=0.9,
        system="You are document analyzing assistant",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "\nAnalyze the image!\n\n"
                                f"\n\n '''\nHuman: ''' \n\n\n'''Summarize the image provided"
                    }
                ]
            }
        ]
    )
    print(message.content)
