import scrapy
from ecom.models import Produit,Categorie


class MyspiderSpider(scrapy.Spider):
    name = "ProductScrap"
    category = None
    start_urls = []

    def __init__(self, category=None, *args, **kwargs):
        super(MyspiderSpider, self).__init__(*args, **kwargs)
        self.category = category
        self.start_urls = [f"https://www.jumia.ma/{self.category}/"]

    def parse(self, response):
        for products in response.css("article.prd"):
            Produit.objects.create(nom=products.css("h3.name::text").get(),prix=products.css("div.prc::text").get(),image=products.css("img::attr(data-src)").get(),categorie = Categorie.objects.get(slug=self.category))
          