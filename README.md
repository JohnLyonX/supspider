#### Supspider 超级蜘蛛

为何要使用Supspider,因为Supspider结合了优秀网络框架的优点,使得这个库更加方便以及简单

例如:

- req = supspider.GetPage('https://y.qq.com/').get_div(',').save('div.html')
  在这里使用了supspider库里面的GetPage,直接获取了页面里面的所有div信息,并且保存在了一个名字叫div.html的文件中

- 在这里面还内置了header请求头部,即使在你没有特殊要求的情况下也可以直接获取到页面

---

- GetPage(url,header) 发起请求
- get_html() 获取整个html页面
- get_body() 获取整个body元素
- get_div(sep) 获取所有div元素
- save(filename,encoding)保存文件
