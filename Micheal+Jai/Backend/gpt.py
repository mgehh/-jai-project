print(";lsdkjsdpfljdspfkj")
# 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
import openai
openai.api_key = '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'

prompt = "Make a joke about farting in class"

response = openai.Completion.create(engine = "text-davinci-001", prompt = prompt, max_tokens = 6)

print(response)