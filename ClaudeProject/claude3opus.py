import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="your-api-key",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    top_p=1,
    messages=[
        {"role": "user", "content": "Hey Claude!"},
        {"role": "assistant", "content": "How can I help you with"},
        {"role": "user", "content": "Can you elaborate the meaning of life in Marathi only"}
    ]
)
print(message.content)
