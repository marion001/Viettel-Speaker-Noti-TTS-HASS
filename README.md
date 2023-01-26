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
          voice_type: 'nu_mien_bac_01'    
          speed: '0.9'   #tốc độ giọng (có giá trị 0.7 - 1.3, tương ứng tốc độ đọc từ x0.7 đến x1.3 lần).
 
#Cấu hình Xong check config rồi khởi động lại home assistant

Lưu Ý: Token Key chỉ dùng được 180 ngày. hết 180 ngày tạo token khác thay vào