import json
import urllib.request

from lxml import etree


# 获取静态页面
class GetPage:
    _init_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    def __init__(self, url, headers=None):
        if headers is not None:
            self.use_headers = self._init_headers
        else:
            self.use_headers = headers
        self.url = url
        self.tree = None
        self.content = None
        self.parse_list = []
        self.value = None
        self._handle_request()

    def __str__(self):
        return str(self.value)

    def _handle_request(self):
        req = urllib.request.Request(self.url, self.use_headers)
        rep = urllib.request.urlopen(req)
        self.tree = etree.HTML(rep.read().decode("UTF-8"))
        self._parsing_robot(self.tree)
        return self

    def _parsing_robot(self, container):
        if type(container) is list:
            for item in container:
                item_content = etree.tostring(item, encoding="UTF-8").decode("UTF-8")
                self.parse_list.append(item_content)
            return self.parse_list
        self.content = etree.tostring(container, encoding="UTF-8").decode("UTF-8")
        return self.content

    def get_html(self):
        document_content = self.content
        self.value = document_content
        return self

    def save(self, filename, encoding="utf-8"):
        if self.content is None:
            raise ValueError("get_response must be called before save.")

        if filename is not None:
            with open(filename, "w", encoding=encoding) as file:
                file.write(self.content)
            return self
        else:
            raise ValueError("Filename must be provided for saving.")

    def get_body(self):
        body_content = self.tree
        body_content = body_content.xpath("/html/body")[0]
        self.value = self.content = self._parsing_robot(body_content)
        return self

    def get_div(self, sep=","):
        div_content = self.tree
        div_content = div_content.xpath("//div")
        self.content = f"{sep}".join(self._parsing_robot(div_content))
        self.value = self._parsing_robot(div_content)
        return self
