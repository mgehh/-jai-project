print(";lsdkjsdpfljdspfkj")
# your token
import openai
openai.api_key = 'your_token'

prompt = "Make a joke about farting in class"

response = openai.Completion.create(engine = "text-davinci-001", prompt = prompt, max_tokens = 6)

print(response)
