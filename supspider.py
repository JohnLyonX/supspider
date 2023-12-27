import requests
from lxml import etree


class Obtain:
    _init_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    def __init__(self, url, method="GET", dp=None, headers=None):
        self.url = url
        self.method = method
        self.dp = dp
        if headers is not None:
            self.use_headers = self._init_headers
        else:
            self.use_headers = headers
        self._handle_request()

    def _handle_request(self):
        if self.method == "GET":
            self._handle_get()
        elif self.method == "POST":
            self._handle_post()
        else:
            return ValueError("unknown method")
        return self

    def _handle_get(self):
        self.rep = requests.get(self.url, params=self.dp, headers=self.use_headers)

    def _handle_post(self):
        self.rep = requests.post(self.url, data=self.dp, headers=self.use_headers)

    def doc(self):
        return self.rep.text

    def edoc(self, path, i=None, encoding="utf-8"):
        doc_tree = etree.HTML(self.rep.text)
        if i is None:
            element = doc_tree.xpath(path)[0]
        else:
            element = doc_tree.xpath(path)[i]
        return etree.tostring(element).decode(encoding)

    def json(self):
        return self.rep.json()


class W:
    def __init__(self, d, n, mode='w', encoding=None):
        self.content = d
        self.name = n
        self.mode = mode
        self.encoding = encoding
        self.value = None
        self._w()

    def __str__(self):
        return f"Object of class W with name: {self.name}, method: {self.mode}, encoding: {self.encoding}"

    def _w(self):
        if self.content is None:
            raise ValueError("The content cannot be blank.")
        elif self.name is None:
            raise ValueError("Filename must be provided for saving.")

        try:
            with open(self.name, self.mode, encoding=self.encoding) as f:
                content = self.content
                if isinstance(content, bytes):
                    content = content.decode(self.encoding)
                f.write(content)
        except Exception as e:
            raise ValueError(f"Failed to write content to file: {str(e)}")
