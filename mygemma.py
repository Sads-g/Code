import huggingface_hub
from huggingface_hub import InferenceClient

def askbot(question, conversation_history=[]):

    client = InferenceClient(
        "meta-llama/Meta-Llama-3-8B-Instruct",
        token="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" #other key dads(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)
    )

    # Append the current question to the conversation history
    conversation_history.append(("user", question))

    response = client.chat_completion(
        messages=[{"role": "user", "content": f"{question}"}],
        max_tokens=500,
        stream=True
    )

    full_response = ""
    for message in response:
        full_response += message.choices[0].delta.content

    # Append the chatbot's response to the conversation history
    conversation_history.append(("bot", full_response))
    return full_response
while True:
    e =input("queustion")
    z=askbot(e)
    print(z)
    if e =="quit":
        break