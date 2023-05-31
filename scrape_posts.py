import requests
from bs4 import BeautifulSoup
from datetime import date

# List to store the scraped post content
post_contents = []
scraped_urls = set()  # Set to store the scraped post URLs



def scrape_posts():
    # Make a request to the Hacker News website
    response = requests.get("https://thehackernews.com")

    # Get the HTML content of the webpage
    html_content = response.content

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the articles on the page
    articles = soup.find_all("div", class_="body-post clear")

    # Get today's date
    today = date.today()

    # Iterate over each article and extract the title, body, and image
    for article in articles:
        # Extract the post date
        post_date = article.find("div", class_="item-label").text

        # Extract the title
        title = article.find("h2", class_="home-title").text

        # Extract the body
        body = article.find("div", class_="home-desc").text

        # Extract the image
        image_element = article.find("img")
        image_url = image_element["src"]

        # Extract the URL
        url = article.find("a")["href"]

        # Check if the post date is today's date and the URL hasn't been scraped before
        if str(today) in post_date and url not in scraped_urls:
            # Store the post content
            post_content = {
                "title": title,
                "body": body,
                "image_url": image_url
            }
            post_contents.append(post_content)
            # Add the URL to the set of scraped URLs
            scraped_urls.add(url)




