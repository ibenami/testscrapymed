from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class OldHealthGovIl(BasePortiaSpider):
    name = "www.old.health.gov.il"
    allowed_domains = [u'www.old.health.gov.il']
    start_urls = [{u'url': u'https://www.old.health.gov.il/units/pharmacy/trufot/Ycran_ListN.asp?p=1&Letter=[a-z]&Sr_Type=Activ&safa=e',
                   u'fragments': [{u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'https://'},
                                  {u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'www.old.health.gov.il/units/pharmacy/trufot/Ycran_ListN.asp?p='},
                                  {u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'1'},
                                  {u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'&Letter='},
                                  {u'valid': True,
                                   u'type': u'range',
                                   u'value': u'a-z'},
                                  {u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'&Sr_Type=Activ&safa=e'}],
                   u'type': u'generated'},
                  u'https://www.old.health.gov.il/units/pharmacy/trufot/',
                  u'https://www.old.health.gov.il/units/pharmacy/trufot/Ycran_ListN.asp?p=1&Letter=n&Sr_Type=Activ&safa=e']
    rules = [
        Rule(
            LinkExtractor(
                allow=(
                    u'https:\\/\\/www\\.old\\.health\\.gov\\.il\\/units\\/pharmacy\\/trufot\\/Ycran_ListN\\.asp\\?p=[1-9]&Letter=[a-z]&Sr_Type=Activ&safa=e',
                    u'https:\\/\\/www\\.old\\.health\\.gov\\.il\\/units\\/pharmacy\\/trufot\\/Mucar_List\\.asp\\?p=\\d&Sr_Type=Activ&Y_Name=(.)*&Letter=[a-z]&safa=e',
                    u'https:\\/\\/www\\.old\\.health\\.gov\\.il\\/units\\/pharmacy\\/trufot\\/PerutTrufa\\.asp\\?Reg_Number=.*&safa=e',
                    u'https:\\/\\/www\\.old\\.health\\.gov\\.il\\/units\\/pharmacy\\/trufot\\/Ycran_ListN\\.asp\\?p=[1-9]&Sr_Type=Activ&Y_Name=&Letter=[a-z]&safa=e'),
                deny=()),
            callback='parse_item',
            follow=True)]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1), table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1)',
                [
                    Field(
                        u'route',
                        'table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(4) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(4) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(4) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(4) > td:nth-child(2) *::text',
                        []),
                    Field(
                        u'tradename_heb',
                        'table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(3) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(3) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(3) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(3) > td:nth-child(2) *::text',
                        []),
                    Field(
                        u'tradename',
                        'table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(2) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(2) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(2) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(2) > td:nth-child(2) *::text',
                        []),
                    Field(
                        u'dosage',
                        'table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(5) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(5) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(5) > td:nth-child(2) *::text, table:nth-child(4) > tr:nth-child(1) > td > table:nth-child(1) > tr:nth-child(5) > td:nth-child(2) *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                '',
                [
                    Field(
                        u'regnumlink',
                        '',
                        [])])]]
