import anthropic
import openai

openai.api_key = "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"

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="sk-ant-api03-8s69j6wlhnFhisMdsyrm43pQnwFM15qNb25YHv8ydvgMMpWw0tyTytdq-"
            "ZY52u_UcJs-R9LwCqNOf791K_a-8g-X61SywAA",
)
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, world"},
        {"role": "assistant", "content": "Hi, I' Claude, how can I help you?"},
        {"role": "user", "content": "Provide me with a code that can analyze the document and "
                                    "generate the results as per the user's prompt"
         }
    ]
)
print(message.content)

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        dict(role="system", content="You are a Language Translator"),

        dict(role="user", content="What is this word Haven?")
    ]
)
print(completion.choices[0].message.content)
