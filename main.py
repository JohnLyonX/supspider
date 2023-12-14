from lxml import etree
import urllib
import seaborn

import supspider

req = supspider.GetPage('https://y.qq.com/').get_div('').save('div.html')
print(req)
