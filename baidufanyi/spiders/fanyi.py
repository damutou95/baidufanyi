# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy import FormRequest, Request
import pymysql
import json
import execjs
import random
import re
from baidufanyi.items import BaidufanyiItem
from baidufanyi import settings
from scrapy_splash import SplashRequest
class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    #allowed_domains = ['sss']
    start_urls = ['https://fanyi.baidu.com/basetrans']
    headers = settings.HEADERS
    filepath = settings.FILEPATH
    headers2 = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

    def start_requests(self):
        url = 'https://fanyi.baidu.com/langdetect'
        yield Request(url=url, callback=self.parse, dont_filter=True, headers=self.headers2, meta={'tag': 0})

    def parse(self, response):
        url = 'https://fanyi.baidu.com/'
        yield Request(url=url, callback=self.parsePlus, dont_filter=True, headers=self.headers2, meta={'tag': 0})

    def parsePlus(self, response):
        token = re.findall("token: '(.*?)',", response.text)[0]
        url = 'https://fanyi.baidu.com/'
        print(token)
        yield Request(url=url, callback=self.parsePP, dont_filter=True, headers=self.headers2, meta={'tag': 0})

    def parsePP(self, response):
        gtk = re.findall("gtk: '(.*?)'", response.text)[0]
        token = re.findall("token: '(.*?)',", response.text)[0]
        print(token)
        #paras = {'gtk': gtk, 'token': token}
        jsCode = f"""
                C = '{gtk}'
                function a(r,o){{
                     for (var t = 0; t < o.length - 2; t += 3) {{
                            var a = o.charAt(t + 2);
                            a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                        }}
                        return r
                }}

                function Tk(r){{
                        var o = r.length;
                        o > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(o / 2) - 5, 10) + r.substr(-10, 10));
                        var t = void 0,
                        n = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
                        t = null !== C ? C : (C = window[n] || "") || ""; 
                        for (var e = t.split("."), h = Number(e[0]) || 0, i = Number(e[1]) || 0, d = [], f = 0, g = 0; g < r.length; g++) {{
                            var m = r.charCodeAt(g);
                            128 > m ? d[f++] = m : (2048 > m ? d[f++] = m >> 6 | 192 : (55296 === (64512 & m) && g + 1 < r.length && 56320 === (64512 & r.charCodeAt(g + 1)) ? (m = 65536 + ((1023 & m) << 10) + (1023 & r.charCodeAt(++g)),
                            d[f++] = m >> 18 | 240,
                            d[f++] = m >> 12 & 63 | 128) : d[f++] = m >> 12 | 224,
                            d[f++] = m >> 6 & 63 | 128),
                            d[f++] = 63 & m | 128)
                        }}
                        for (var S = h, u = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), l = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), s = 0; s < d.length; s++)
                            S += d[s],
                            S = a(S, u);
                        return S = a(S, l),
                        S ^= i,
                        0 > S && (S = (2147483647 & S) + 2147483648),
                        S %= 1e6,
                        S.toString() + "." + (S ^ h)
                }}
                """
        js = execjs.compile(jsCode)

        with open(self.filepath, 'r') as f:
            kws = f.readlines()
            for kw in kws:
                keyword = kw.strip()
                formdata = {
                    'query':  keyword,
                    'from':  'zh',
                    'to':  'en',
                    'simple_means_flag': '3',
                    'sign': js.call('Tk', keyword),
                    'token': token
                }
                headers = {
                    # 'Accept':  '*/*',
                    # 'Accept-Encoding':  'gzip, deflate, br',
                    # 'Accept-Language':  'zh-CN,zh;q=0.9',
                    # 'Connection':  'keep-alive',
                    # #'Content-Length':  '96',
                    # 'Content-Type':  'application/x-www-form-urlencoded',
                    # 'Cookie':  'BAIDUID=92D7E68170373AC3900003967D6B6B40:FG=1; BIDUPSID=92D7E68170373AC3900003967D6B6B40; PSTM=1546563918; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; IMG_WH=414_736; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; rsv_i=686a7iZtZTZU0YXQaWAO2txunF9cjaQ1c9%2BwF2uW%2BnmGciAh4ZD2ZjW7K%2BFxdUQ3Wv4JtvJTq7NGex3RfubsEmL2Epjj8sQ; FEED_SIDS=71898_0128_14; H_WISE_SIDS=127980_126886_125818_127694_114550_127237_129070_126170_128066_127491_128853_120124_123019_128713_118879_118868_118842_118827_118789_128037_107312_126996_129180_127771_127404_129087_127768_128448_117430_128451_128818_128402_129079_129036_127029_128789_129010_128967_128247_128805_128771_127797_114819_126720_124030_128341_110085_123289_127125_128763_128807_127319_128600_127416_129251_128961_100459; SE_LAUNCH=5%3A25810970; PSINO=6; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1548658270; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1548658270; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1548653153,1548653173,1548656635,1548658270; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1548658270',
                    # 'Host':  'fanyi.baidu.com',
                    # 'Origin':  'https://fanyi.baidu.com',
                    'Referer':  'https://fanyi.baidu.com/',
                    'User-Agent':  'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
                    #'X-Requested-With':  'XMLHttpRequest',
                }
                yield FormRequest(self.start_urls[0], formdata=formdata, callback=self.parsePPP, headers=headers, dont_filter=True, meta={'tag': 0})

    def parsePPP(self, response):
        item = BaidufanyiItem()
        item['translation'] = json.loads(response.text)['trans'][0]['dst']
        item['original'] = json.loads(response.text)['trans'][0]['src']
        yield item
