# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import unicodedata


def remove_currency(value):
    return value.replace('Kn', '').strip()

def remove_new_line(value):
    return value.replace('\n    ', '').replace('\n      ', '').strip()

def remove_space(value):
    return value.replace(" ", "_").strip()

def remove_unicode(value):
    return value.encode("ascii", "ignore").decode()

def normalize_unicode(value):
    return str(unicodedata.normalize('NFKD', value).encode('ascii', 'ignore'))[2:-1 ]

def comma_to_dot(value):
    return value.replace(",", ".")

def toString(value):
    if value[0] != '"':
        value = '"' + value
    if value[-1] != '"':
        value = value + '"'
    return str(value)

class HackscraperItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags, remove_new_line, normalize_unicode, toString), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency, comma_to_dot, toString), output_processor=TakeFirst())
    link = scrapy.Field(input_processor=MapCompose(toString))
    tag = scrapy.Field(input_processor=MapCompose(remove_tags, remove_new_line, remove_space, normalize_unicode, toString), output_processor=TakeFirst())
    store = scrapy.Field(input_processor=MapCompose(toString))

    pass


