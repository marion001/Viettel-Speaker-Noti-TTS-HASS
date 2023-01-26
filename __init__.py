#encoding: utf-8
import requests
import json
import os
import urllib
DOMAIN = 'viettel_speaker'
CFG_Noti = 'noti'
CFG_TokenKey = 'Key' #Cấu hình Token Key trong configuration.yaml
CFG_Http_Hass = 'Url_Hass' 
CFG_ID_Speaker_Hass = 'entity_id'
CFG_NoiDung = 'message'
def setup(hass, cfg):
    def xuly_dulieu(get_dulieu):
        Id_Speak_Hass = get_dulieu.data.get(CFG_ID_Speaker_Hass)
        Ten_File_TTS = 'Viettel_Speaker_Noti.mp3'
        headers = {'Content-type': 'application/json', 'token': str(cfg[DOMAIN][CFG_TokenKey])}
        data = {'text': str(get_dulieu.data.get(CFG_NoiDung)), "voice": "hn-quynhanh", "id": "2", "without_filter": False, "speed": "0.8", "tts_return_option": 3}
        response = requests.post("https://viettelgroup.ai/voice/api/tts/v1/rest/syn", data=json.dumps(data), headers=headers, verify=False)
        f = open("/config/www/Viettel_Speaker/"+Ten_File_TTS, 'wb')
        f.write(response.content)
        f.close()
        Http_File_Mp3 = str(cfg[DOMAIN][CFG_Http_Hass])+"/local/Viettel_Speaker/"+Ten_File_TTS
        Data_Hass = {'entity_id': Id_Speak_Hass, 'media_content_id': Http_File_Mp3, 'media_content_type': 'audio/mp3'}
        hass.services.call('media_player', 'play_media', Data_Hass)
    hass.services.register(DOMAIN, CFG_Noti, xuly_dulieu)
    return True
