import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
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