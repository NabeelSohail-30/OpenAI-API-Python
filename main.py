# Import openai
import openai

# Set your API key
openai.api_key = "<OPENAI_API_TOKEN>"

# Create a request to the Completion endpoint
response = openai.Completion.create(
  # Specify the correct model
  model="text-davinci-003",
  prompt="Who developed ChatGPT?"
)

print(response)

# Extract the model from the response
print(response['model'])

# Extract the total_tokens from the response
print(response["usage"]["total_tokens"])

# Extract the text from the response
print(response['choices'][0]['text'])

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=100
)

# Extract and print the response text
print(response["choices"][0]["text"])

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the expectation of obtaining an added income or profit in return. There are a variety of investment options available, including stocks, bonds, mutual funds, real estate, precious metals, and currencies. Making an investment decision requires careful analysis, assessment of risk, and evaluation of potential rewards. Good investments have the ability to produce high returns over the long term while minimizing risk. Diversification of investment portfolios reduces risk exposure. Investment can be a valuable tool for building wealth, generating income, and achieving financial security. It is important to be diligent and informed when investing to avoid losses."""

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  max_tokens=400,
  temperature=0.5
)

print(response["choices"][0]["text"])

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Create a slogan for a new restaurant.",
  max_tokens=100
)

print(response["choices"][0]["text"])

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="""Classify sentiment as negative, positive, or neutral:
    1. Unbelievably good!
    2. Shoes fell apart on the second use.
    3. The shoes look nice, but they aren't very comfortable.
    4. Can't wait to show them off!
  """,
  max_tokens=100
)

print(response['choices'][0]['text'])

# Create a request to the Completion endpoint
response = openai.Completion.create(
 model="text-davinci-003",
 prompt="Categorize the following list of companies as either Tech, Energy, Luxury Goods, or Investment: Apple, Microsoft, Saudi Aramco, Alphabet, Amazon, Berkshire Hathaway, NVIDIA, Meta, Tesla, LVMH",
 max_tokens=100,
 temperature=0.5
)

print(response['choices'][0]['text'])


# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system",
     "content": "You are a helpful data science tutor."},
    {"role": "user",
     "content": "What is the difference between a for loop and a while loop?"}
  ]
)

# Extract the assistant's text response
print(response['choices'][0]['message']['content'])

instruction = """Explain what this Python code does in one sentence:
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan": 1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful Python programming assistant."},
    {"role": "user", "content": instruction}
  ],
  max_tokens=100
)

print(response['choices'][0]['message']['content'])

# Create a request to the ChatCompletion endpoint
response = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   # Add a user and assistant message for in-context learning
   messages=[
     {"role": "system", "content": "You are a helpful Python programming tutor."},
     {"role": "user", "content": "Explain what the min() function does."},
     {"role": "assistant", "content": "The min() function returns the smallest item from an iterable."},
     {"role": "user", "content": "Explain what the type() function does."}
   ]
)

print(response['choices'][0]['message']['content'])

messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
  print("User: ", q)

  # Create a dictionary for the user message from q and append to messages
  user_dict = {"role": "user", "content": q}
  messages.append(user_dict)

  # Create the API request
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=100
  )

  # Convert the assistant's message to a dict and append to messages
  assistant_dict = dict(response["choices"][0]["message"])
  messages.append(assistant_dict)
  print("Assistant: ", response["choices"][0]["message"]["content"], "\n")


# Create a request to the Moderation endpoint
response = openai.Moderation.create(
  model="text-moderation-latest",
  input="My favorite book is How to Kill a Mockingbird."
)

print(response["results"][0]["category_scores"])


# Open the openai-audio.mp3 file
audio_file = open("openai-audio.mp3", "rb")

# Create a transcript from the audio file
response = openai.Audio.transcribe("whisper-1", audio_file)

# Extract and print the transcript text
print(response["text"])

# Open the audio.m4a file
audio_file= open("audio.m4a", "rb")

# Create a transcript from the audio file
response = openai.Audio.transcribe("whisper-1", audio_file)

print(response["text"])


# Open the audio.m4a file
audio_file = open("audio.m4a", "rb")

# Create a translation from the audio file
response = openai.Audio.translate("whisper-1", audio_file)

# Extract and print the translated text
print(response["text"])

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "The transcript contains a discussion on a recent World Bank Report."

# Create a translation from the audio file
response = openai.Audio.translate("whisper-1",
                                  audio_file,
                                  prompt=prompt)

print(response["text"])


# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Create a transcription request using audio_file
audio_response = openai.Audio.transcribe("whisper-1", audio_file)

# Create a request to the API to identify the language spoken
chat_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a languages specialist."},
    {"role": "user", "content": "Identify the language used in the following text: " + audio_response["text"]}
  ]
)
print(chat_response["choices"][0]["message"]["content"])


# Open the datacamp-q2-roadmap.mp3 file
audio_file = open("datacamp-q2-roadmap.mp3", "rb")

# Create a transcription request using audio_file
audio_response = openai.Audio.transcribe("whisper-1", audio_file)

# Create a request to the API to summarize the transcript into bullet points
chat_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "List the courses that DataCamp will be making as bullet points." + audio_response["text"]}
  ],
  max_tokens=100
)
print(chat_response["choices"][0]["message"]["content"])

