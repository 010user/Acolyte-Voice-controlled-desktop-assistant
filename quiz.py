import speech_recognition as sr
import pyttsx3



def speak(key):
    #TEXT TO SPEECH
    engine = pyttsx3.init()
    engine.say(key)
    engine.runAndWait()

#####################################################################################

def listen():
    #LISTEN TO USER AND RETURN WITH TEXT
    r = sr.Recognizer()  # OBJECT OF RECOGNIZER CLASS FROM SR LIBRARY
    with sr.Microphone() as source:
        print("Speak your answer (a/b/c/d).")
        speak("Speak your answer.")
        print("Listening....")
        audio = r.listen(source, phrase_time_limit=3)
    try:
        text = r.recognize_google(audio, language='en')
        text = text.lower()
        print("You said : {}".format(text))
        if text=='a' or text=='b' or text=='c' or text=='d':
            print()
        else:
            print("Invalid input")
            speak("Invalid Input. Please type your answer.")
            text = str(input("Please type your answer: "))
    except:
        print("Invalid input")
        speak("Invalid Input. Please type your answer.")
        text = str(input("Please type your answer: "))
    return text




#######################################################################################


######TECHNICAL
def askqt():
        score =0
        #Question 1
        print("1. 'OS' computer abbreviation usually means ? \nA.Order of Significance \nB.Open Software \nC.Operating System \nD.Optical Sensor")
        speak("'OS' computer abbreviation usually means ? \nA)Order of Significance \nB)Open Software \nC)Operating System \nD)Optical Sensor")
        ta1 = listen()
        if ta1=='c' or ta1=='C' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score, "\n")

        #Question 2
        print("2. Who co-founded Hotmail in 1996 and then sold the company to Microsoft? \nA.Shawn Fanning \nB.Ada Byron Lovelace\nC.Sabeer Bhatia\nD.Ray Tomlinson")
        speak("2. Who co-founded Hotmail in 1996 and then sold the company to Microsoft? \nA)Shawn Fanning \nB)Ada Byron Lovelace\nC)Sabeer Bhatia\nD)Ray Tomlinson")
        ta2 = listen()
        if ta2=='c' or ta2=='C' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 3
        print("3. '.gif' is and extension of  \nA.Word File \nB.Image File \nC.Audio File\nD.Video File")
        speak("3. '.gif' is and extension of  \nA)Word File \nB)Image File \nC)Audio File\nD)Video File")
        ta3 = listen()
        if ta3=='b' or ta3=='B' :
            score +=1
            print("Correct Answer","\n")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is B")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 4
        print("4. Which among following first generation of computers had ?\nA.Vaccum Tubes and Magnetic Drum \nB.Integrated Circuits\nC.Magnetic Tape and Transistors\nD.All of above")
        speak("4. Which among following first generation of computers had ?\nA)Vaccum Tubes and Magnetic Drum \nB)Integrated Circuits\nC)Magnetic Tape and Transistors\nD)All of above")
        ta4 = listen()
        if ta4=='a' or ta4=='A' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is D")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 5
        print("5. Full form of URL is ?\nA.Uniform Resource Locator\nB.Uniform Resource Link\nC.Uniform Registered Link\nD.Unified Resource Link")
        speak("5. Full form of URL is ?\nA)Uniform Resource Locator\nB)Uniform Resource Link\nC)Uniform Registered Link\nD)Unified Resource Link")
        ta5 = listen()
        if ta5=='a' or ta5=='A' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is A")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        # FINAL MESSAGE
        if score<=1:
            print("Your total score is :",score,"out of 5. See you in next quiz")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. See you in next quiz")
        elif 2<=score<=3:
            print("Your total score is :",score,"out of 5. You went ok")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. You went ok")
        else:
            print("Your total score is :",score,"out of 5. Well played !!")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. Well played !!")



######General Knowledge
def askqg():
        score = 0
        #Question 1
        print("\n1. For which of the following disciplines is Nobel Prize awarded?\nA.Physics and Chemistry \nB.Physiology or Medicine \nC.Literature, Peace and Economics \nD.All of the above")
        speak("\n1. For which of the following disciplines is Nobel Prize awarded?\nA)Physics and Chemistry \nB)Physiology or Medicine \nC)Literature, Peace and Economics \nD)All of the above")
        ga1 = listen()
        if ga1=='d' or ga1=='D' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is D")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 2
        print("2. Each year International Yoga Day is celebrated on\nA.May 8 \nB.May 18 \nC.June 21\nD.June 18")
        speak("2. Each year International Yoga Day is celebrated on\nA)May 8 \nB)May 18 \nC)June 21\nD)June 18")
        ga2 = listen()
        if ga2=='c' or ga2=='C' :
            score +=1
            print("Correct Answer","\n")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 3
        print("3. Guru Gobind Singh was\nA.the 10th Guru of the Sikhs \nB.founder of Khalsa, the inner council of the Sikhs in 1699\nC.author of Dasam Granth \nD.All the above")
        speak("3. Guru Gobind Singh was\nA)the 10th Guru of the Sikhs \nB)founder of Khalsa, the inner council of the Sikhs in 1699\nC)author of Dasam Granth \nD)All the above")
        ga3 = listen()
        if ga3=='d' or ga3=='D' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is D")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        #Question 4
        print("4. Golden Temple, Amritsar is India's \nA.largest Gurdwara \nB.oldest Gurudwara\nC.Both option A and B are correct\nD.None of the above")
        speak("4. Golden Temple, Amritsar is India's \nA)largest Gurdwara \nB)oldest Gurudwara\nC)Both option A and B are correct\nD)None of the above")
        ga4 = listen()
        if ga4=='a' or ga4=='A' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is A")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 5
        print("5. Dr. Zakir Hussain was\nA.first vice president of India\nB.the first Muslim president of India\nC.first president of Indian National Congress\nD.first speaker of Lok Sabha")
        speak("5. Dr. Zakir Hussain was\nA)first vice president of India\nB)the first Muslim president of India\nC)first president of Indian National Congress\nD)first speaker of Lok Sabha")
        ga5 = listen()
        if ga5=='b' or ga5=='B' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is B")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        # FINAL MESSAGE
        if score<=1:
            print("Your total score is :",score,"out of 5. See you in next quiz")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. See you in next quiz")
        elif 2<=score<=3:
            print("Your total score is :",score,"out of 5. You went ok")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. You went ok")
        else:
            print("Your total score is :",score,"out of 5. Well played !!")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. Well played !!")


######SPORTS


def askqs():
        score = 0
        #Question 1
        print("\n1. Which among the following country was the host of 2010 Commonwealth Games?\nA.Canada \nB.England \nC.Australia \nD.India")
        speak("\n1. Which among the following country was the host of 2010 Commonwealth Games?\nA)Canada \nB)England \nC)Australia \nD)India")
        sa1 = listen()
        if sa1=='d' or sa1=='D' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is D")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 2
        print("2. The word “Agricultural shot” is known to be used sometimes in which among the following sports?\nA.Cricket \nB.Hockey \nC.Golf\nD.Polo")
        speak("2. The word “Agricultural shot” is known to be used sometimes in which among the following sports?\nA)Cricket \nB)Hockey \nC)Golf\nD)Polo")
        sa2 = listen()
        if sa2=='a' or sa2=='A' :
            score +=1
            print("Correct Answer","\n")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is A")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 3
        print("3. With which game is Major Dhyanchand associated?\nA.Lawn Tennis\nB.Kabbadi\nC.Hockey\nD.Cricket")
        speak("3. With which game is Major Dhyanchand associated?\nA)Lawn Tennis\nB)Kabbadi\nC)Hockey\nD)Cricket")
        sa3 = listen()
        if sa3=='c' or sa3=='C' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        #Question 4
        print("4. Who is named as the Flying Sikh of India?\nA.Ajit Pal Singh \nB.Joginder Singh\nC.Milkha Singh\nD.Mohinder Singh")
        speak("4. Who is named as the Flying Sikh of India?\nA)Ajit Pal Singh \nB)Joginder Singh\nC)Milkha Singh\nD)Mohinder Singh")
        sa4 = listen()
        if sa4=='c' or sa4=='C' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 5
        print("5. Hima Das is famous in which sport?\nA.Lawn Tennis\nB.Field and Track\nC.Hockey\nD.Women's Cricket")
        speak("5. Hima Das is famous in which sport?\nA)Lawn Tennis\nB)Field and Track\nC)Hockey\nD)Women's Cricket")
        sa5 = listen()
        if sa5=='b' or sa5=='B' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is B")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        # FINAL MESSAGE
        if score<=1:
            print("Your total score is :",score,"out of 5. See you in next quiz")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. See you in next quiz")
        elif 2<=score<=3:
            print("Your total score is :",score,"out of 5. You went ok")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. You went ok")
        else:
            print("Your total score is :",score,"out of 5. Well played !!")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. Well played !!")


######BOLLLYWOOD



def askqb():
        score = 0
        #Question 1
        print("\n1. Who played the infamous villain Gabbar in 'Sholay'?\nA.Pran \nB.Ajit \nC.Kader Khan\nD.Amjad Khan")
        speak("\n1. Who played the infamous villain Gabbar in 'Sholay'?\nA)Pran \nB)Ajit \nC)Kader Khan\nD)Amjad Khan")
        ba1 = listen()
        if ba1=='d' or ba1=='D' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is D")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 2
        print("2.Nominated in the Best Foreign film category at the Oscars, Mother India lost to:\nA.Casablanca \nB.Nights of Cabiria\nC.Gone With The Wind\nD.Dragons")
        speak("2.Nominated in the Best Foreign film category at the Oscars, Mother India lost to:\nA)Casablanca \nB)Nights of Cabiria\nC)Gone With The Wind\nD)Dragons")
        ba2 = listen()
        if ba2=='b' or ba2=='B' :
            score +=1
            print("Correct Answer","\n")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is B")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 3
        print("3. Who directed the Shahrukh Khan, Madhuri Dixit and Aishwarya Rai-starrer 'Devdas'?\nA.Sanjay Leela Bhansali\nB.Prakash Jha\nC.Ashutosh Gowariker\nD.Karan Johar")
        speak("3. Who directed the Shahrukh Khan, Madhuri Dixit and Aishwarya Rai-starrer 'Devdas'?\nA)Sanjay Leela Bhansali\nB)Prakash Jha\nC)Ashutosh Gowariker\nD)Karan Johar")
        ba3 = listen()
        if ba3=='a' or ba3=='A' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is A")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        #Question 4
        print("4. Who composed the music in Ashutosh Gowariker’s period drama 'Jodhaa Akbar'?\nA.Shankar-Ehsaan-Loy\nB.Anu Malik\nC.Jatin-Lalit\nD.A.R. Rahman")
        speak("4. Who composed the music in Ashutosh Gowariker’s period drama 'Jodhaa Akbar'?\nA)Shankar-Ehsaan-Loy\nB)Anu Malik\nC)Jatin-Lalit\nD)A R Rahman")
        ba4 = listen()
        if ba4=='d' or ba4=='D' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")

        #Question 5
        print("5. Which of these Amitabh Bachchan films had the tagline 'It’s all about loving your parents'?\nA.Paa \nB.Baghban\nC.Kabhi Khushi Kabhi Gham\nD.Waqt")
        speak("5. Which of these Amitabh Bachchan films had the tagline 'It’s all about loving your parents'?\nA)Paa \nB)Baghban\nC)Kabhi Khushi Kabhi Gham\nD)Waqt")
        ba5 = listen()
        if ba5=='c' or ba5=='C' :
            score +=1
            print("Correct Answer")
            speak("Correct Answer")
            print("Score :",score,"\n")
        else:
            print("Incorrect !! Correct Answer is C")
            speak("Incorrect !! Correct Answer is C")
            print("Score :",score,"\n")


        # FINAL MESSAGE
        if score<=1:
            print("Your total score is :",score,"out of 5. See you in next quiz")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. See you in next quiz")
        elif 2<=score<=3:
            print("Your total score is :",score,"out of 5. You went ok")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. You went ok")
        else:
            print("Your total score is :",score,"out of 5. Well played !!")
            speak("Your total score is :")
            speak(score)
            speak("out of 5. Well played !!")



# askqt()
# askqg()
# askqs()
# askqb()