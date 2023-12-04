import scrapy
import json
import re

class FlatsSpider(scrapy.Spider):
    """
    Spider for crawling a real estate website to extract listings of flats.

    Attributes:
        name: Name of the spider.
        number_of_flats: Total number of flats to scrape.
        category_type: Type of the category (e.g., buy, rent).
        category_main: Main category of the listings.
        start_urls: URLs where the spider begins to crawl.
    """
    name = 'flats'
    number_of_flats = 500  # Define the number of flats you want to scrape
    category_type = 1      # 1 represents the category type (e.g., 1 for buy)
    category_main = 1      # 1 represents the main category (e.g., 1 for flat)

    # Starting URL for scraping data
    start_urls = [
        f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb={category_main}&category_type_cb={category_type}&page=0&per_page={number_of_flats}'
    ]

    def parse(self, response, **kwargs):
        """
        Parse the JSON response from the website and extract relevant data.

        Args:
            response: The response object to parse.

        Yields:
            A dictionary of the extracted flat data.
        """
        try:
            # Parse the JSON response
            response_json = json.loads(response.text)

            # Iterate over each estate in the response
            for estate in response_json.get('_embedded', {}).get('estates', []):
                title = estate.get('name', 'No title available').strip()
                title = re.sub(r'\s+', ' ', title)  # Clean up whitespace in the title

                # Extract the first image URL, if available
                image_url_list = estate.get('_links', {}).get('images', [])
                image_url = image_url_list[0].get('href', 'No image URL') if image_url_list else 'No image URL'

                # Yield the extracted data as a dictionary
                yield {'title': title, 'image_url': image_url}

        except json.JSONDecodeError:
            self.logger.error('Error decoding JSON')
        except Exception as e:
            self.logger.error(f'An error occurred: {e}')
