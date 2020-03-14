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





### WebSocket的四类事件



- Socket.onopen 连接建立时触发

- Socket.onmessage 客户端接收服务端数据时触发

- Socket.oneerror 通信发生错误时触发

- Socket.onclose 连接关闭时触发



### WebSocket方法



- Socket.send()  使用连接发送数据 

- Socket.close()  关闭连接



## WebSocket在django下的实现

### dwebsocket

https://github.com/duanhongyi/dwebsocket

#### decorators 

- accept_websocket 

- require_websocket

  

#### middlewares

- MIDDLEWARE_CLASSES = ['dwebsocket.middleware.WebSocketMiddleware']
- WEBSOCKET_ACCEPT_ALL = True

#### python request object

- request.is_websocket()
- reqeust.websocket
  - Websocket.wait(timeout=-1)
  - Websocket.read()
  - Websocket.count_messages()
  - Websocket.has_messages()
  - Websocket.send(message)
  - Websocket._______iter__()
  - Websocket.is_closed()
  - 

![image-20200314180042585](/Users/huangjiani/Library/Application Support/typora-user-images/image-20200314180042585.png)













