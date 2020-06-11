import sys
import re
# import server
#from .server import app
#from convertData import convert_data_mode_1
import convertData
import server
import time
import threading
import requests
import exportExcel

idr_thread=[]
def mode1():
    print("ban dang vao che do gui 1 goi data co dinh\n")  
    print("nhap chuoi data ban muon gui:")
    data=input()
    print("nhap so chuoi data muon gui:")
    total=input()
    print("Nhap thoi gian cho vong lap:")
    time_loop=int(input())
    #while(data[0]=='I' and data[6]=='T' and data[9]=='H' and data[13]=='O' and data[17]=='B' and len(data)==21):
    #while data[0]!='I' and data[7]!='H' and data[11]!='O' and data[15]!='B' and len(data)==19:   
    while True:
        if data[0]=='I' and data[6]=='H' and data[10]=='O' and data[14]=='B' and len(data)==18:
        #if data[0]=='I' and data[1]=='D' and data[7]=='H' and data[11]=='O'and len(data)==15:
            break
        #print("nhap chuoi chua dung format yeu cau format \"IxxxxxTxxHxxxOxxxBxxx\"\n")
        print("nhap chuoi chua dung format yeu cau format \"IxxxxxHxxxOxxxBxxx\"\n")
        print("nhap lai chuoi data:")
        data=input()
    convertData.convert_data_mode_1(data)
    i=0
    server.connect_server(convertData.msg)
    while(i<int(total)):
        server.reconnect()
        server.mqttc.publish(server.MQTT_TOPIC,convertData.msg)
        #server.mqttc.subscribe(MQTT_TOPIC)
        #server.mqttc.disconnect()
        #server.send_data_server(convertData.msg)
        time.sleep( time_loop)
        i+=1
 
def mode2():
    print("Ban dang vao che do random ")
    print("nhap gia tri ID cua thiet bi dau :")
    idrMin=int(input())
    print("nhap gia tri ID cua thiet bi cuoi :")
    idrMax=int(input())
    print("nhap so chuoi data muon gui:")
    total=input()
    print("Nhap thoi gian cho vong lap:")
    time_loop=int(input())
    print("nhap gia tri heartRate Min:")
    HrMin=int(input())
    print("nhap gia tri hearRate Max:")
    HrMax=int(input())
    print("nhap gia tri Oxy Min:")
    OxyMin=int(input())
    print("nhap gia tri Oxy Max:")
    OxyMax=int(input())
    print("nhap gia tri Beat Min:")
    BeatMin=int(input())
    print("nhap gia tri Beat yMax:")
    BeatMax=int(input())
    convertData.conver_data_mode_2(idrMin,idrMax,HrMin,HrMax,OxyMin,OxyMax)
    i=0 
    server.connect_server(convertData.msg)
    while(i<int(total)):
        convertData.conver_data_mode_2(idrMin,idrMax,HrMin,HrMax,OxyMin,OxyMax,BeatMin,BeatMax)
        server.reconnect()
        server.mqttc.publish(server.MQTT_TOPIC,convertData.msg)
        time.sleep( time_loop)
        i+=1
    
def mode3():
    print("ban dang vao che do gui goi data multithread:\n")  
    print("nhap so thread:")
    num_of_thread=int(input())
    for i in range(0,num_of_thread):
        print("nhap id thiet bi gui o thread["+str(i)+"]:")
        idr_thread.append(input())
    print("nhap so vong lap cho multithread:")
    total=int(input())
    print("Nhap thoi gian delay cho vong lap multithread:")
    time_loop=int(input())
    print("nhap gia tri heartRate Min:")
    HrMin=int(input())
    print("nhap gia tri hearRate Max:")
    HrMax=int(input())
    print("nhap gia tri Oxy Min:")
    OxyMin=int(input())
    print("nhap gia tri Oxy Max:")
    OxyMax=int(input()) 
    print("nhap gia tri Beat Min:")
    BeatMin=int(input())
    print("nhap gia tri Beat yMax:")
    BeatMax=int(input())
    j=0
    thread_array=[]
    server.connect_server(convertData.msg)
    while(j<total):
        t=time.time() 
        for i in range(0,num_of_thread):
            idr=idr_thread[i]
            convertData.conver_data_mode_3( idr,HrMin,HrMax,OxyMin,OxyMax,BeatMin,BeatMax)
            thread_instance=threading.Thread(target=server.mqttc.publish(server.MQTT_TOPIC,convertData.msg), args=(convertData.msg,))
            thread_obj={
                "name":"t"+str(i),
                "thread":thread_instance
            }   
            thread_array.append(thread_obj)
        for thread_obj in thread_array:
            thread_obj["thread"].start()
        for thread_obj in thread_array:
            thread_obj["thread"].join()
        thread_array.clear()
        j+=1
        time.sleep(time_loop)
def choice(i):
    if(i=='1'):
        mode1()
    elif(i=='2'):
        mode2()
    elif(i=='3'):
        mode3()
    else:
        main()
def main():
    # print("nhap host: ")
    # host=input()
    # print("nhap port: ")
    # port=input()
    # print("nhap url:")
    # server.url=input()
    # print("nhap web API:")
    # server.api_url=input()
    print("chon mode:")
    mode=0
    mode=input()
    choice_mode=choice(mode)
    print("So goi data gui thanh cong: "+str(server.count))
    server.count=0
    #exportExcel.export_excel()
    print("tiep tuc?(Y/N):")
    temp=input()
    if temp=="Y" or temp=="y": 
        main() 
    if temp !='Y':
        pass
    
if __name__ == "__main__":
    main()
   