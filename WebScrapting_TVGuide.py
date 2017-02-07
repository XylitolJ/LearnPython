import requests
from bs4 import BeautifulSoup as bs
import csv
import os

"""Get info video from tvgui"""

urls = ['http://www.tvguide.com/tvshows/in-an-instant/episodes/760326/',
        'http://www.tvguide.com/tvshows/in-an-instant/episodes-season-1/760326/']

os.chdir(r'C:\Users\DELL\PycharmProjects\Example')

css_selector_episode = 'p.tvobject-episode-episodic-info'
css_selector_title = 'div.tvobject-episode-meta-info.hidden-xs > p.tvobject-episode-episodic-info'  # title css selector
css_selector_title2 = 'h4'  # title css selector
css_selector_p = 'p.tvobject-episode-description.hidden-xs'  # paragraph css selector
css_selector_date = 'p.tvobject-episode-airdate.hidden-xs'  # date release css selector
for url in urls:
    res = requests.get(url)     # assign result to 'res' variable
    res.raise_for_status()      # raise Error if download not success

    soup = bs(res.text, "html.parser")     # Using BeautifulSoup to normalize html
    element_title = soup.select(css_selector_title)
    element_episode = soup.select(css_selector_episode)
    element_title2 = soup.select(css_selector_title2)
    element_p = soup.select(css_selector_p)
    element_date = soup.select(css_selector_date)

    with open('tvgui_insaninstant.csv', 'a', newline='') as csvfile:
        writercsv = csv.writer(csvfile)
        for episode, title, title2, p, date in zip(element_episode, element_title, element_title2, element_p, element_date):
            writercsv.writerow([episode.text, title.text, title2.text, p.text.strip(), date.text])

