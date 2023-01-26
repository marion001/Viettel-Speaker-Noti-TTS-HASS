#encoding: utf-8
import requests
import json
import os
import time
import urllib
import datetime

DOMAIN = 'viettel_speaker'
CFG_Noti = 'noti'
CFG_Key = 'Key'                         #Cấu hình Token Key trong configuration.yaml
CFG_Speed = 'speed'
CFG_Http_Hass = 'Url_Hass'              #Cấu hình Url_Hass trong configuration.yaml  http://192.168.xxx.xxx:8123
CFG_ID_Speaker_Hass = 'entity_id'
CFG_NoiDung = 'message'


def setup(hass, cfg):
    def xuly_dulieu(get_dulieu):
        #Biến Config
        Token_Key = str(cfg[DOMAIN][CFG_Key])
        Http_Hass = str(cfg[DOMAIN][CFG_Http_Hass])
        Id_Speak_Hass = get_dulieu.data.get(CFG_ID_Speaker_Hass)
        Noi_Dung_Thong_Bao = str(get_dulieu.data.get(CFG_NoiDung)[0:2000])
        Toc_Do_Doc = get_dulieu.data.get(CFG_Speed)
        Ten_File_TTS = 'Viettel_Speaker_Noti.mp3'
        
        url = 'https://viettelgroup.ai/voice/api/tts/v1/rest/syn'
        headers = {'Content-type': 'application/json', 'token': Token_Key}
        data = {'text': Noi_Dung_Thong_Bao, "voice": "hn-quynhanh", "id": "2", "without_filter": False, "speed": Toc_Do_Doc, "tts_return_option": 3}
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        f = open("/config/www/Viettel_Speaker/"+Ten_File_TTS, 'wb')
        f.write(response.content)
        f.close()
        
        # Ghép URL File http://192.168.xxx.xxx:8123/local/tts/xxxxx.mp3
        Http_File_Mp3 = Http_Hass+"/local/Viettel_Speaker/"+Ten_File_TTS
        
        Service_Data = {'entity_id': Id_Speak_Hass, 'media_content_id': Http_File_Mp3, 'media_content_type': 'audio/mp3'}
        hass.services.call('media_player', 'play_media', Service_Data)
        
    hass.services.register(DOMAIN, CFG_Noti, xuly_dulieu)
    return True
