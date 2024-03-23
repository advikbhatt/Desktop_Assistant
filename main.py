import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import numpy as np
import win32com.client
# Use your own choice sapi.spvoice according to the version that will be available
speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "Enter Your OPEN AI API KEY HERE"
    chatStr += f"Advik: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        print("Error:", e)
        return "I'm sorry, I couldn't generate a response."

def ai(prompt):
    openai.api_key = "Enter Your OPEN AI API KEY HERE"
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = openai.Completion.create(
            model="text-davinci-001",
            # Use the latest Version of the model that will be available at the time of reading this article.
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print("Error:", e)

def say(text):
    speaker.Speak(f'{text}')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "Some Error Occurred."

if __name__ == '__main__':
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if():
            pass

        elif "the time" in query:
            now = datetime.datetime.now()
            say(f"The time is {now.hour} hours {now.minute} minutes")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
