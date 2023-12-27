### Supspider 超级蜘蛛

---

##### 1. 为何使用?

- 结合了优秀网络库以及原生Python的操作,让实现效果的代码更加简短

##### 2. 有何特点?

- 2.1. 降低学习成本,更快上手,更加简单
- 2.2. 让爬虫程序更加简单再简单
- 2.3. 语法简短,更优雅的编码风格

阶段: 完善中,欢迎参与开发

目前提供的方法:

- 1.1. get
- 1.2. post

API:

请求方法:
<br>
Obtain(url,method,dp(data or params),headers(默认拥有简单的请求头))

- doc() 获取整个html文档
- edoc(path,index,encoding) 获取指定标签, path: 标签路径用法和Xpath一致, index: 标签索引(默认为None), encoding: 编码(
  默认为utf-8)
- json() 获取json数据

写入:
<br>
W(content, filename, mode(默认为'w'写入模式), encoding(默认为utf-8))

开始使用:
```python
import supspider as sp

# 获取博客的body,并写入body.html
rep = sp.Obtain("http://www.lyonjohn.xyz", "GET").edoc("/html/body")
print(rep)
sp.W(rep, "body.html")
