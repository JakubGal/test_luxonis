# pipelines.py: Defines item pipelines for Scrapy project

import psycopg2
import logging

class PostgresPipeline:
    """
    Pipeline for storing scraped items in a PostgreSQL database.
    """

    def open_spider(self, spider):
        """
        Called when the spider is opened. Establishes a connection to the database
        and truncates the 'flats' table to remove any existing data.
        """
        # Connect to PostgreSQL database
        self.connection = psycopg2.connect(host='db', dbname='flats_db', user='luxonis', password='admin')
        self.cursor = self.connection.cursor()

        # Truncate the table to start fresh each time the spider is run
        self.cursor.execute("TRUNCATE TABLE flats RESTART IDENTITY;")
        self.connection.commit()

    def close_spider(self, spider):
        """
        Called when the spider is closed. Closes the database connection.
        """
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        """
        Called for each item pipeline component. Inserts the item into the database.
        """
        try:
            # Insert item into 'flats' table
            self.cursor.execute("INSERT INTO flats (title, image_url) VALUES (%s, %s)", 
                                (item['title'], item['image_url']))
            self.connection.commit()
        except psycopg2.DatabaseError as e:
            # Log any database errors
            logging.error(f"Database error: {e}")

        return item
