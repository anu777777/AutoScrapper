# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:25:41 2021

@author: win10
"""

from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/iphone/s?k=iphone"

wanted_list=["₹71,999","Apple iPhone 14 (128 GB) - Yellow"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))

scraper.set_rule_aliases({'rule_4fq4':'Title','rule_4gax':'Price'})
scraper.keep_rules(['rule_4fq4','rule_4gax'])
scraper.save('amazon-search')
