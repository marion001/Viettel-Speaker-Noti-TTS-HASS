# Viettel-Speaker-Noti-TTS-HASS
Bước 1:

+,đi tới thư mục "custom_components" và tạo thư Mục tên "viettel_speaker".
  tiếp theo tải 2 file "__init__.py" và "manifest.json" vào trong thư mục "viettel_speaker" vừa tạo.
  
+,Tạo tiếp thư mục "www" ngang hàng với file "configuration.yaml". 
  tiếp đến vào thư mục "www" vừa tạo, tạo tiếp một thư mục nữa có tên là: "Viettel_Speaker"

#tạo xong check config rồi khởi động lại Home Assistant

Bước 2:
Tạo tài khoản + tạo token tại đây: https://viettelgroup.ai/dashboard/token


#Cấu Hình trong file configuration.yaml theo bên dưới đây:

      viettel_speaker:
        Key: 'M98myd7lWRT23z9kaRCgYv3DQsbjfyojLJW3ZJ29zNlF********************' #Thay Token Của Bạn vào đây
        Url_Hass: 'http://192.168.xxx.xxx:8123'  #Thay Địa CHỉ Hass Local CỦa Bạn tại đây hoặc Domain


#cấu hình input text để nhập văn bản thành giọng nói 

      input_text:
        viettell_tts_text:
          name: "Nhập Nội Dung"
 
#Cấu hình trong file script.yaml

    viettel_speaker:
      sequence:  
      - service: tts_viettel.say
        data_template:
          entity_id: media_player.googlehomemini    
          message: '{{ states(''input_text.viettell_tts_text'') }}'
 
#Cấu hình Xong check config rồi khởi động lại home assistant

# Cấu hình lovelace:

    type: custom:vertical-stack-in-card
    cards:
      - artwork: cover
        entity: media_player.googlehomemini
        hide:
          icon_state: false
          power_state: false
          runtime: false
          source: false
          volume: false
        icon: mdi:google-assistant
        type: custom:mini-media-player
        name: Loa Google Home Mini
        info: short
      - type: entities
        entities:
          - entity: input_text.viettell_tts_text
            icon: mdi:message-processing
            name: 'Nhập Nội Dung:'
          - entity: script.viettel_speaker
            name: 'Gửi Thông Báo:'
            icon: mdi:cast-audio


Lưu Ý: Token Key chỉ dùng được 180 ngày. hết 180 ngày tạo token khác thay vào


