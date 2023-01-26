import openai

input_here = input("Enter your Question: ")
API_KEY = 'Your API key'
openai.api_key = API_KEY
model = 'text-davinci-003'
response = openai.Completion.create(
    prompt=input_here,
    model=model,
    max_tokens=2000,
)

for obj in response.choices:
    print(obj.text)
