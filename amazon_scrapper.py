#!/usr/bin/env python
# coding: utf-8

# In[6]:


import scrapy
file=open("DATA.txt","w")


# In[7]:


class MySpider(scrapy.Spider):
    name = "amazon_spider"
    
    def start_requests(self):
        urls = ["https://www.amazon.in/s?k=mobiles&qid=1559161835&ref=sr_pg_1",
                "https://www.amazon.in/s?k=mobiles&page=2&qid=1559161835&ref=sr_pg_2",
                "https://www.amazon.in/s?k=mobiles&page=3&qid=1559161835&ref=sr_pg_3",
                "https://www.amazon.in/s?k=mobiles&page=4&qid=1559162393&ref=sr_pg_4",
                "https://www.amazon.in/s?k=mobiles&page=5&qid=1559162403&ref=sr_pg_5"
               ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        page_id=response.url[-1]
        filename = "amazon %s.html"%page_id
        
        with open(filename,'wb') as f:
            f.write(response.body)
            
        
        phone=response.xpath('//span[@class="a-size-medium a-color-base a-text-normal"]/text()').getall()
        
        price = response.xpath('//span[@class="a-price-whole"]/text()').getall()
        
        rating = response.xpath('//span[@class="a-icon-alt"]/text()').getall()
        
        people_who_rated = response.xpath('//span[@class="a-size-base"]/text()').getall()
        
        
        for s in phone:
            i=phone.index(s)
            file.write(s)
            file.write("\n")
            file.write(price[i])
            file.write("\n")
            file.write(rating[i])
            file.write(" rated by ")
            file.write(people_who_rated[i])
            file.write(' people')
            file.write("\n\n")
        self.log("Saved File %s"%filename)


# In[ ]:




