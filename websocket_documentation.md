# 基于WebSocket实现的多人聊天室

我选择作业中的HTML5高级应用技术之Websocket框架进行开发实践。

## WebSocket简介

### 什么是WebSocket？

Websocket协议是一个基于TCP的协议，由通信协议和编程API组成，能够在浏览器和服务器之间建立双向连接。

它是HTML5开始提供的一种在单个TCP连接上进行全双工通讯的协议。

WebSocket 使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在 WebSocket API 中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。

在 WebSocket API 中，浏览器和服务器只需要做一个握手的动作，然后，浏览器和服务器之间就形成了一条快速通道。两者之间就直接可以数据互相传送。

现在，很多网站为了实现推送技术，所用的技术都是 Ajax 轮询。轮询是在特定的的时间间隔（如每1秒），由浏览器对服务器发出HTTP请求，然后由服务器返回最新的数据给客户端的浏览器。这种传统的模式带来很明显的缺点，即浏览器需要不断的向服务器发出请求，然而HTTP请求可能包含较长的头部，其中真正有效的数据可能只是很小的一部分，显然这样会浪费很多的带宽等资源。

HTML5 定义的 WebSocket 协议，能更好的节省服务器资源和带宽，并且能够更实时地进行通讯。



### 和HTTP协议有什么不同？

HTTP协议是基于浏览器请求——服务器响应的流程完成的，而WebSocket作为双向通信，服务器端和客户端可以同时发送并且响应请求。



### 与传统ajax轮询的对比

传统ajax轮询需要定时发送ajax请求给服务器端查找数据，服务器端（根据是长轮询还是短轮询）响应返回数据给客户端，一方面效率很低，另一方面当客户端连接数目很大时，很有可能会超过服务器端能承受的最大TCP连接数量。

而websocket在一次http握手之后，便可理解为形成了双向的数据通路，服务器端可以不断在这个连接上给客户端推送数据，无论是实时性还是效率都远胜传统ajax轮询。



### WebSocket的四类事件

- Socket.onopen 连接建立时触发

- Socket.onmessage 客户端接收服务端数据时触发

- Socket.oneerror 通信发生错误时触发

- Socket.onclose 连接关闭时触发



### WebSocket方法

- Socket.send()  使用连接发送数据 

- Socket.close()  关闭连接



## WebSocket在django下的实现

### dwebsocket框架

https://github.com/duanhongyi/dwebsocket

通过pip3 install dwebsocket下载之后，配置settings.py即可直接在相应的services中进行调用。

#### decorators 装饰器定义

- @accept_websocket 可以接受http和websocket请求，通过is_websocket()来判断两者

- @require_websocket 只能接受websocket请求


#### middlewares 中间件定义

在settings.py中引入相关的中间件

- MIDDLEWARE_CLASSES = ['dwebsocket.middleware.WebSocketMiddleware']
- WEBSOCKET_ACCEPT_ALL = True

#### python request object

使用的reqeust相关属性说明

- request.is_websocket()
- reqeust.websocket
  - Websocket.wait(timeout=-1) 阻塞式
  - Websocket.read() 非阻塞式
  - Websocket.count_messages() 消息数量
  - Websocket.has_messages() 判断是否有消息
  - Websocket.send(message) 发送
  - Websocket._______iter__() 返回迭代器
  - Websocket.is_closed() 判断是否关闭

## 项目实战

- 后端：Django，python下的web框架

- 前端：Jquery

  项目效果如图所示：

  ![image-20200315092514951](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200315092514951.png)

  

  - 新用户进入聊天室，系统随机生成昵称和user_id，用户也可自定义昵称（但只能修改一次）。

    ![image-20200315092600304](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200315092600304.png)

  - 多位用户加入群聊，左栏为历史聊天记录，右栏为在线用户列表。

    ![image-20200315092724586](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200315092724586.png)

  - 其中某一位用户离开聊天室，在用户列表上删除该用户。

  ![image-20200315092807022](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200315092807022.png)

### 视图文件views.py

- to_chat(request): render the index.html

- chat(request):  websocket connection 

- msg_send(request): send msg

- change_name(request): change the name

  主体代码如图所示：

  ![image-20200315093816533](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200315093816533.png)

### 模版文件index.html

（因代码量较少，未把连接websocket的js脚本另外放置在static目录下，而是直接内嵌模版文件中）

![image-20200315094035122](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200315094035122.png)













