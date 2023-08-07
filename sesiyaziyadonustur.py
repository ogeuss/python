#burada kütüphaneyi import ediyorum.
import speech_recognition
import pyttsx3

#tanıyıcıyı tanımlıyoruz
taniyici = speech_recognition.Recognizer()

# mikrofonu program hata vermedikçe ve kapatılmadıkça dinlemesini bunu yazıya türkçe dilinde dökmesini 
# ve küçük harflerle ekrana yazdırmasını söylüyorum. 
while True:
    try:
        with speech_recognition.Microphone() as mic:
            taniyici.adjust_for_ambient_noise(mic, duration=0.2)
            ses= taniyici.listen(mic)
            yazi = taniyici.recognize_google(ses, language="tr")
            yazi = yazi.lower()
            print(f"Kayıt:{yazi}")
    except speech_recognition.UnknownValueError():
         taniyici = speech_recognition.Recognizer()
         continue
            