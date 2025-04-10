from django.apps import apps
from celery import shared_task
import helpers


@shared_task
def scrape_product_url_task(url):
    if url is None:
        return 
    elif url == "":
        return
    productScrapeEvent = apps.get_model('products', 'ProductScrapeEvent')
    html= helpers.scrape(url=url)
    data=helpers.extract_amazon_product_data(html)
    productScrapeEvent.objects.create_scrape_event(data=data, url=url)
    return

@shared_task
def scrape_product_task():
    Product = apps.get_model('products', 'Product')
    qs=Product.objects.filter(active=True)
    for obj in qs:
        url=obj.url
        scrape_product_url_task.delay(url=url)
