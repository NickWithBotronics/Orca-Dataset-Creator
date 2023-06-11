import os
import openai
import json

# Assuming you have your API key in an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load dataset
with open('alpaca_52k.jsonl', 'r') as f:
    dataset = [json.loads(line) for line in f]

def ask_gpt(instruction, system):
    response = openai.Completion.create(
        engine="text-davinci-003.5",  # use the appropriate engine for GPT-3.5
        prompt=f"{system}\n{instruction}",
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Iterate through dataset and ask GPT-3.5
for data in dataset:
    instruction = data["instruction"]
    system = f"The user is an 8-year-old child who needs a step-by-step, simplified explanation of how to {instruction}"
    answer = ask_gpt(instruction, system)
    print(f"Instruction: {instruction}\nAnswer: {answer}\n")
