from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random

class RandomUserAgentMiddleware(UserAgentMiddleware):
    """
    Middleware to set a random User-Agent for each request.
    
    This helps in mimicking different browser types and potentially
    avoiding detection as a bot by some websites.
    """

    # List of user agents to choose from
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        # Add more user agents here as needed
    ]

    def process_request(self, request, spider):
        """
        Method called for each request made by the spider.
        It randomly selects a user agent from the list and sets it in the request header.
        """
        # Randomly select a user agent and set it in the request header
        random_user_agent = random.choice(self.user_agents)
        request.headers.setdefault('User-Agent', random_user_agent)
