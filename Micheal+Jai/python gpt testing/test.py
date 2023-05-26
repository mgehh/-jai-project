#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
import openai

openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "write a haiku poem about Michael Geh"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)