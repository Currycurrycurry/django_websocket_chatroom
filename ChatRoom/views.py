from django.shortcuts import render
from django.shortcuts import HttpResponse 
from dwebsocket.decorators import accept_websocket 
import uuid
import json

USER_MSG = 0
TXT_MSG = 1


def to_chat(request):
    return render(request,'index.html')


clients = {}
client_names_dict = dict()
@accept_websocket
def chat(request):
    print("server: enter the websocket")
    if request.is_websocket():
        userid=str(uuid.uuid1())[:8]
        clients[userid] = request.websocket
        
        while True:
            message=request.websocket.wait() # block
            if not message:
                break
            else:
                msg=str(message, encoding = "utf-8")
                print(msg)
                msg, user_name = msg.split("_")
                if msg == "test":
                    print("客户端链接成功："+userid)
                    client_names_dict[userid] = user_name
                    request.websocket.send(json.dumps({"type":USER_MSG,"user_list":list(client_names_dict.values()), "user_id":userid, "user_name":user_name}).encode("'utf-8'"))
                    for client in clients:
                        clients[client].send(json.dumps({"type":USER_MSG,"user_list":list(client_names_dict.values()),"user":None}).encode("'utf-8'"))
    if userid in clients:
        del clients[userid]
        del client_names_dict[userid]
        print(userid + "离线")
        for client in clients:
            clients[client].send(
                json.dumps({"type": USER_MSG, "user_list": list(client_names_dict.values()), "user": None}).encode("'utf-8'"))

def msg_send(request):
    msg = request.POST.get("txt")
    # useridto = request.POST.get("userto")
    useridfrom = request.POST.get("user_from")
    # type=request.POST.get("type")
    print(request.POST)
    for client in clients:
        clients[client].send(json.dumps({"type": TXT_MSG,"data": {"msg": msg, "user_id":useridfrom, "user_name": client_names_dict[useridfrom]}}).encode('utf-8'))
    return HttpResponse(json.dumps({"msg":"success"}))

def change_name(request):
    msg = request.POST.get("user_name")
    useridfrom = request.POST.get("user_from")
    client_names_dict[useridfrom] = msg
    return HttpResponse(json.dumps({"msg":"success"}))


