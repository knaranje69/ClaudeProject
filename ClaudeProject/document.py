import anthropic
import os

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="your-api-key",
)
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1001,
    temperature=0.9,
    system="You are my document assistant",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "\nAnalyze the string!\n"
                            "\n\n '''\nHuman: '''My name is Kshitij, I'm 23 years old'''\n'''What is the name of the "
                            "person'''\n"
                            "\n\n'''\nHuman: '''I am passionate about my hobbies and the time I invest in my day to "
                            "day life'''\n"
                            "'''\nWhat is the sentiment of this text?'''"
                }
            ]
        }
    ]
)
print(message.content)
