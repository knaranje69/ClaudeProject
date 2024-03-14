import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="your-api-key",
)

image_path = "MLOps.jpg"
response = client.messages.create(image_path)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    top_p=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "pdf/jpg",
                        "data": "image_data",
                    },
                },
                {
                    "type": "text",
                    "text": "Describe what is in the document"
                }
            ],
        }

    ],
)
print(message.content)
