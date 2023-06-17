import openai

openai.api_key = "keyCode" #keyCode is your API key

answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "QUESTION" #Here we ask the question and provide the codesnippet

 }])

print(answer) #prints the answer from ChatGPT in the console
