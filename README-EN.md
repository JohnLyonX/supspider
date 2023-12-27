### Supspider

---

##### 1. Why use?

- It combines excellent network libraries and native Python operations to make the code to achieve the effect shorter.

##### 2. What are the characteristics?

- 2.1. Reduce learning costs, get started faster, and be simpler
- 2.2. Make the crawler program simpler and simpler
- 2.3. Short syntax, more elegant coding style

Stage: Under development, welcome to participate in development

Currently provided methods:

- 1.1. get
- 1.2. post

API:

Request method:
<br>
Obtain(url,method,dp(data or params),headers(By default there are simple request headers))

- doc() Return the entire html document
- edoc(path,index,encoding) Get the specified label, path: Tag path usage is consistent with Xpath, index: Tag index (default is None), encoding: coding(
  Default is utf-8)
- json() Get json data

Write:
<br>
W(content, filename, mode (default is 'w' writing mode), encoding (default is utf-8))

start using:
```python
import supspider as sp

# Get the body of the blog and write it into body.html
rep = sp.Obtain("http://www.lyonjohn.xyz", "GET").edoc("/html/body")
print(rep)
sp.W(rep, "body.html")
