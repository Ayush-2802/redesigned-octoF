#!/usr/bin/python3
import datetime
import sys
import webbrowser
from urllib.request import urlopen

import aiml
from bs4 import BeautifulSoup as bs
import requests
import wikipedia
import wolframalpha
import bs4
from app_opening_function import *
from get_input import *

try:
    BRAIN_FILE = "res/brain.dump"
    k = aiml.Kernel()
    hour: int = int(datetime.datetime.now().hour)

    if os.path.exists(BRAIN_FILE):
        k.loadBrain(BRAIN_FILE)
    else:
        k.bootstrap(learnFiles="res/std-startup.aiml", commands="load aiml b")
        k.saveBrain(BRAIN_FILE)

    if 0 <= hour < 12:
        assistant_speaks("Good Morning!")

    elif 12 <= hour < 18:
        assistant_speaks("Good Afternoon! ")

    else:
        assistant_speaks("Good Evening! ")

    if __name__ == "__main__":
        while 1:
            text: str = get_audio()
            try:
                if "exit" in str(text) or "bye" in str(text) or "shut up" in str(text) or "sleep" in str(text) in input:
                    print("sleep mode to activate press shift + F ")
                    break

                elif "who are you" in text or 'hello' in text or 'what is your name' in text:
                    speak = '''Hello, I am Friday. Your personal Assistant.
                        I am here to make your life easier.You can command me to perform various tasks such ascalculating sums, weather report, general conversation, web searching,or opening applications etcetra'''
                    assistant_speaks(speak)

                elif 'wikipedia' in text:
                    try:
                        query = text.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        assistant_speaks('Searching Wikipedia...')
                        assistant_speaks("According to Wikipedia")
                        print(results)
                        assistant_speaks(results)
                    except:
                        assistant_speaks("No internet connection")

                elif 'play music' in text:
                    try:
                        music_dir = 'C:\\Users\\Aditi Ayush\\Music'
                        songs = os.listdir(music_dir)
                        a = enumerate(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))
                        print(" to veiw song list song list (press s)")
                        ch = input(">")
                        if ch == "s":
                            print(a)
                        else:
                            print("no songs found")

                    except Exception as g:
                        if g == "list index out of range":
                            print("no songs found")
                        else:
                            print("i ran out of songs")

                elif "WEATHER" in text or "weather" in text or "Weather" in text:
                    try:
                        ch = ""
                        if "of" in text:
                            ch = "of"
                        else:
                            ch = "in"
                        a = text.lower().split().index(ch)
                        b = text.split()[a + 1:]
                        c = ' '.join([str(elem) for elem in b])
                        place = c
                        place = place.replace(" ", "-")
                        url = "https://www.weather-forecast.com/locations/" + place + "/forecasts/latest"
                        r = requests.get(url)
                        soup = bs(r.content, "html.parser")
                        weather = soup.findAll("span", {"class": "phrase"})[0].text
                        assistant_speaks(weather)
                        sys.stdout.flush()
                    except:
                        assistant_speaks("no internet connection")

                elif "who made you" in text or "created you" in text:
                    speak = "I have been created by Mr. Ayush Mishra."
                    assistant_speaks(speak)

                elif "calculate" in text.lower():
                    try:
                        app_id = "E46YXW-T5LG6RT7K7"
                        client = wolframalpha.Client(app_id)

                        indx = text.lower().split().index('calculate')
                        query = text.split()[indx + 1:]
                        res = client.query(' '.join(query))
                        answer = next(res.results).text
                        assistant_speaks("The answer is " + answer)
                    except:
                        assistant_speaks("no internet connection")

                elif 'news' in text:
                    try:
                        news_url = "https://news.google.com/news/rss"
                        url_a = urlopen(news_url)
                        xml_page = url_a.read()
                        url_a.close()

                        soup_page = bs4.BeautifulSoup(xml_page, "html.parser")
                        news_list = soup_page.findAll("item")
                        # Print news title and publisher
                        news: text
                        assistant_speaks('Here are today top 10 news from google news')
                        for news in news_list[:10]:
                            a = news.title.text
                            assistant_speaks(a)
                            print("-" * 75)
                    except:
                        assistant_speaks("no internet connection")

                elif 'open' in text:
                    open_application(text.lower())


                elif 'search' in text:
                    try:
                        a = text.lower().split().index('search')
                        b = text.split()[a + 1:]
                        c = ' '.join([str(elem) for elem in b])

                        assistant_speaks('searching as new tab in webbrowser')
                        url = "https://www.google.com.tr/search?q={}".format(c)
                        webbrowser.open_new_tab(url)
                    except:
                        assistant_speaks("no internet connection")

                else:
                    response = k.respond(text)
                    assistant_speaks(response)

            except Exception as f:
                # print(f)
                break
except Exception as x:
    while True:
        print (x)
