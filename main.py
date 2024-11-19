from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.findAll(class_='titleline', name='span')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.a.getText()
    article_texts.append(text)
    link = article_tag.a.get('href')
    article_links.append(link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name='span', class_='score')]

largest_upvote = max(article_upvotes)
index_of_largest_upvote = article_upvotes.index(largest_upvote)

print(article_texts[index_of_largest_upvote])
print(article_upvotes[index_of_largest_upvote])
print(article_links[index_of_largest_upvote])
# print(article_upvotes[0].split()[0])
# print(soup.prettify())