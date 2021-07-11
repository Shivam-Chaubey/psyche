import speech_recognition as sr


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Please say your story")
        audio = recognizer.listen(source)
        try:
            print("You have said: \n"+recognizer.recognize_google(audio, language="en-IN"))
        except:
            print("Didn't get you.")


if __name__=="__main__":
    main()


