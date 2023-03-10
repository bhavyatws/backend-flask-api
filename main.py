# from bs4 import BeautifulSoup
import requests
# import sys
# print(sys.executable)
import openai
# userget = input("Enter the URL: ")
# requests.get(str(userget))
# url = requests.get(str(userget)).text
# soup = BeautifulSoup(url, 'html.parser')

import openai
import json
def index():
    # Load JSON data from config file
    with open('config.json', 'r') as f:
        config = json.load(f)

    def open_file(file_name):
        with open(file_name, 'r', encoding='utf-8') as infile:
            return infile.read()

    def save_file(file_name, data):
        with open(file_name, 'w', encoding='utf-8') as outfile:
            outfile.write(data)
            
    # #div = soup.find('div', attrs={'class':'hh hi hj hk hl'})
    # try:
    #     text = soup.find_all('p').text   
    # except:
    #     text = soup.find('body').text

            
        
    # docs = open('data.txt', 'a', encoding='utf-8')
    # docs.write(text)
    # docs.close()

    openai.api_key = config['api_key']

    feed = open_file('data.txt')
    prompt = open_file('prompt.txt').replace('<<FEED>>', feed)

    response = openai.Completion.create(
        model = 'text-davinci-002',
        prompt = prompt,
        temperature = 1.0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )

    text = response['choices'][0]['text'].strip()
    print(prompt)
    print(text)

    save_file('output.txt', text)
    prompt1 = open_file('output.txt')

    response = openai.Image.create(
        prompt = prompt1 + ('modern, 8k'),
        n=1,
        size = "1024x1024"
    )

    image_url = response['data'][0]['url']

    URL = image_url
    response = requests.get(URL)
    open('image.png', 'wb').write(response.content)

    

    result = {
        'summary': text,
        'image' : URL
    }
    return result



