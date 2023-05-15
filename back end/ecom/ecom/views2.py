
from twisted.internet import reactor
from django.http import JsonResponse
from crochet import setup, wait_for, TimeoutError
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from jumiascraper.jumiascraper.spiders.myspider import MyspiderSpider
import logging

setup()

@wait_for(timeout=30.0)
def crawl_task(category):
    # Configure logging for Scrapy
    configure_logging()

    # Run Scrapy spider to scrape Jumia products
    runner = CrawlerRunner()
    deferred = runner.crawl(MyspiderSpider, category=category)
    return deferred

def scrape(request, category):
    try:
        crawl_task(category)
        # Return a response indicating success
        return JsonResponse({'message': 'Scraping complete'})
    except TimeoutError as e:
        logging.exception("Crawling took too long")
        return JsonResponse({'message': 'Crawling took too long'})
    except Exception as e:
        logging.exception("Crawling failed: {}".format(str(e)))
        return JsonResponse({'message': 'Crawling failed'})
