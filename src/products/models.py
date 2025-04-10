from django.db import models

from .tasks import scrape_product_url_task

class Product(models.Model):
    asin=models.CharField(max_length=120, unique=True,db_index=True)
    url=models.URLField(null=True, blank=True)
    title=models.CharField(max_length=220,null=True, blank=True)
    current_price=models.FloatField(null=True, blank=True, default=0.00)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    metadata=models.JSONField(null=True, blank=True)
    active=models.BooleanField(default=True, help_text="Scrape Daily?")
    

    # def save(self, *args, **kwargs):
    #     if self.url and self.pk and self.trigger_scrape:
    #         if self.trigger_scrape != self._trigger_scrape:
    #             # Trigger the scrape task
    #             self._trigger_scrape = False
    #             self.trigger_scrape = False
    #             scrape_product_url_task.delay(self.url)
    #     super(Product, self).save(*args, **kwargs)




class ProductScrapeEventManager(models.Manager): 
    def create_scrape_event(self,data, url=None):
        asin=data.get('asin') or None
        if asin is None:
            return None
        product, created =  Product.objects.update_or_create(asin=asin,
                                         defaults={'title':data.get('title') or None, 
                                                   'url':url,
                                                   'current_price':data.get('price') or 0.00, 
                                                   "metadata":data})
        event=self.create(product=product, url=url, data=data, asin=asin) 
        return event

class ProductScrapeEvent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
    url=models.URLField(null=True, blank=True)
    data=models.JSONField(null=True, blank=True)
    asin=models.CharField(max_length=120, null=True, blank=True)
    

    objects = ProductScrapeEventManager()
  