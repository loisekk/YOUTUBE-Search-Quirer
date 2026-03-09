import speech_recognition as sr

def voice_input():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as src:
            print("🎙️ Listening...")
            audio = r.listen(src, timeout=5)
            return r.recognize_google(audio)
    except Exception as e:
        print("⚠️ Voice input unavailable:", e)
        return ""
