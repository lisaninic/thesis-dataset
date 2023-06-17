import openai

openai.api_key = "keyCode" #keyCode is your API key

answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Do these two snippets achieve the same thing? Please answer yes or no."

"from functools import reduce"

"def find_remainder(arr, n):"
"sum_1 = reduce(lambda x, y: x*y, arr)"
"remainder = sum_1 % n"
"print(remainder)"

"arr = [100, 10, 5, 25, 35, 14]"
"n = 11"
"find_remainder(arr, n)"




"arr = [100, 10, 5, 25, 35, 14];lens = len(arr);n = 11"
"mul = 1"
"for i in range(lens):"
"mul = (mul * (arr[i] % n)) % n"
"print(mul % n)" }])

print(answer)
