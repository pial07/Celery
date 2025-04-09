from django.db import models

class Product(models.Model):
    asin=models.CharField(max_length=120, unique=True,db_index=True)



class ProductScrapeEventManager(models.Manager): 
    def get_scrape_event(self,data):
        asin=data.get('asin') or None
        if asin is None:
            return None
        product, created =  Product.objects.update_or_create(asin=asin,
                                         defaults={'title':data.get('title') or None, 
                                                   'current_price':data.get('price') or 0.00, 
                                                   "metadata":data})


class ProductScrapeEvent(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
      
