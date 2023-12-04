# items.py: Defines the data structures for storing scraped data in Scrapy project

import scrapy

class FlatItem(scrapy.Item):
    """
    Scrapy Item for storing information about a flat.
    
    This item is used to structure the scraped data of individual flats.
    Each FlatItem contains a title and an image URL.
    """

    # Title of the flat listing
    title = scrapy.Field()

    # URL of the image associated with the flat listing
    image_url = scrapy.Field()
