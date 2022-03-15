import tempfile

import typer
from bs4 import BeautifulSoup
from requests import get
from rich import print
from rich.traceback import install
from slack_sdk import WebClient


def get_doc(url: str):
    return get(url).text


def count_products(search_class: str, soup: BeautifulSoup):
    products = soup.select(search_class)

    return len(products)


def send_failure(doc, count, channel, token):
    client = WebClient(token=token)

    client.chat_postMessage(channel=channel, text=f"Last 3 days contains {count} products")

    f = tempfile.NamedTemporaryFile()
    f.write(doc.encode('utf-8'))

    try:
        client.files_upload(channels=channel, file=f.name, filename="category.html")
    finally:
        f.close()



def main(url: str, search_class: str, min_products: int, slack_channel: str, slack_token: str):
    doc = get_doc(url)
    soup = BeautifulSoup(doc, 'html.parser')

    count = count_products(search_class, soup)

    if count < min_products:
        send_failure(doc, count, slack_channel, slack_token)

    print(f"{count} products found")


if __name__ == '__main__':
    install(show_locals=True)
    typer.run(main)

# https://slack.com/oauth/v2/authorize?client_id=403998877974.403228695938&scope=chat:write,files:write,incoming-webhook
