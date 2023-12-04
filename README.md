# Project map
```
task_luxonis/
│
├── flask_app/                    # Flask application directory
│   ├── app.py                    # Main Flask application file
│   ├── Dockerfile                # Dockerfile for building the Flask app container
│   ├── requirements.txt          # Python dependencies for the Flask app
│   └── templates/                # Templates directory for Flask
│       └── index.html            # HTML template for displaying the scraped data
│
├── scrapy_project/               # Scrapy project directory
│   ├── scrapy_project/           # Scrapy project's main module
│   │   ├── __init__.py           # Initializes Python module
│   │   ├── items.py              # Defines the Scrapy Item for the scraped data
│   │   ├── middlewares.py        # Custom middleware, e.g., RandomUserAgentMiddleware
│   │   ├── pipelines.py          # Pipeline to process and store scraped data into PostgreSQL
│   │   ├── settings.py           # Settings file for the Scrapy project
│   │   └── spiders/              # Directory containing spiders
│   │       └── flats_spider.py   # Spider to scrape real estate listings
│   ├── Dockerfile                # Dockerfile for building the Scrapy project container
│   ├── requirements.txt          # Python dependencies for the Scrapy project
│   └── scrapy.cfg                # Configuration file for the Scrapy project
│
├── db_init_scripts/              # Directory containing database initialization scripts
│   └── 01_init.sql               # SQL script to initialize the PostgreSQL database
│
├── docker-compose.yml            # Docker Compose file to orchestrate the containers
├── README.md                     # README file for the project documentation
└── .gitignore                    # Specifies intentionally untracked files to ignore
```
# Task
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and 
save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a 
simple page (title and image) and put everything to single docker compose command so that I can just run 
"docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.

## Setup and Installation
To set up and run this project, you need Docker and Docker Compose. Follow these steps:
1. Ensure Docker and Docker Compose are installed and running on your machine
2. Clone this repository:
```
git clone https://github.com/JakubGal/task_luxonis.git
```
3. Navigate to the project directory:
``` 
cd task_luxonis
```
4. Run the Docker Compose command:
```   
docker-compose up
```
5. Access the Flask application at `http://127.0.0.1:8080`.

## Database Schema
The PostgreSQL database consists of a single table, `flats`, with the following schema:
- `id`: Integer, Primary Key, Auto-increment
- `title`: String (max 255 characters), Title of the flat listing
- `image_url`: Text, URL of the image for the flat listing

## Design notes:

#### Using API:
I used API for web scraping for 2 main reasons 
  1. In https://www.sreality.cz/robots.txt it is allowed to use API for data scraping
  2. It is easier for processing

#### Using Flask:
  Flask is ideal for its simplicity, flexibility and it is perfectly 
  fitting the needs of a web scraping display project like this.

## License
This project is open-sourced under the [MIT License](LICENSE).

## Author
Jakub Gál, 2023
