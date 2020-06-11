import re
import json
import random  

idd='0'
heartRate='0'
oxy='0'
# beat='0'
msg='0'
conv_data='0'

def convert_data_mode_1(data):
    global msg
    pattern='I'
    #pattern='ID' 
    result1 = re.split(pattern, data) #tach chuoi thanh 1 list 2 phan tu gom ID và phan con lai(result1)
    pattern='H'
    result2 = re.split(pattern, result1[1]) #tach chuoi result1 thanh 2 phan tu gom data của ID và phan lai(result2)
    pattern='O'
    result3 = re.split(pattern, result2[1])#tach chuoi result2 thanh 2 phan tu gom data cua Heartrate và oxy
    pattern='B'
    result4 = re.split(pattern, result3[1])
    idd=result2[0] #id data nam o result2[0]
    heartRate=result3[0]
    #oxy=result3[1]
    oxy=result4[0]
    beat=result4[1]
    #conv_data='{'+'\'code\':'+'\'''ID'+idd+'H'+heartRate+'O'+oxy+'\''+'}'
    #dt='ID'+idd +'H'+heartRate+'O'+oxy
    dt='I'+idd +'H'+heartRate+'O'+oxy+'B'+beat
    conv_data= {                          #dua chuoi ve dang json
        "code": dt
    }
    msg=json.dumps(conv_data)            #encode json
    print(msg)
    # return idd,heartRate,oxy,beat
    return msg
def conver_data_mode_2(idrMin,idrMax,HrMin,HrMax,OxyMin,OxyMax,BeatMin,BeatMax):           #xu ly radom data cho Heartrate va Oxy
    global msg
    idr=random.randint(idrMin,idrMax)
    heartRate=random.randint(HrMin,HrMax)
    oxy=random.randint(OxyMin,OxyMax)
    beat=random.randint(OxyMin,OxyMax)
    dt='I'+str(idr)+'H'+str(heartRate)+'O'+str(oxy)+'B'+str(beat)
    conv_data= {
        "code": dt
    }
    msg=json.dumps(conv_data)
    return msg
    
def conver_data_mode_3(idr,HrMin,HrMax,OxyMin,OxyMax,BeatMin,BeatMax):           #xu ly radom data cho Heartrate va Oxy
    global msg
    heartRate=random.randint(HrMin,HrMax)
    oxy=random.randint(OxyMin,OxyMax)
    beat=random.randint(OxyMin,OxyMax)
    dt='I'+idr+'H'+str(heartRate)+'O'+str(oxy)+'B'+str(beat)
    conv_data= {
        "code": dt
    }
    msg=json.dumps(conv_data)
    return msg