import requests
from bs4 import BeautifulSoup
import pandas as pd

mimuw_url = "https://www.mimuw.edu.pl"
sample_size = 5

def get_announcements():
    soup = BeautifulSoup(requests.get(mimuw_url).text, "html.parser")

    announcements = []
    for announcement in soup.find_all("div", class_ = lambda name: name and "info-item announcements-item" in name):
        announcements.append({
            "Name": announcement.find("h3").text,
            "Date": announcement.find(class_ = "info-item-text-date").text,
            # "Link": mimuw_url + announcement.find(class_="more").find("a")["href"],
        })
    return announcements

def print_sample(announcements):
    df = pd.DataFrame(announcements)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(df.sample(min(len(df), sample_size)))

def save_to_csv(announcements):
    df = pd.DataFrame(announcements)
    df.to_csv("mimuw_annoucements.csv", index=False, encoding='utf-8')

announcements = get_announcements()
print_sample(announcements)
save_to_csv(announcements)
