# Tú código va aquí

print ("Welcom to your horoscope")

def menu():
    print("Consulta tu signo")
    print("Elige tu signo")
    print("1", "Aries")
    print("2", "taurus")
    print("3", "cancer")
    print("4", "gemini")
    print("5", "leo")
    print("6", "Virgo")
    print("7", "Libra")
    print("8", "scorpio")
    print("9", "sagittarius")
    print("10", "capricornus")
    print("11", "aquarius")
    print("12", "pisces")
    print("exit", "Salida")

def read_file(signs):
   file = open("signs/"+ prediccion,'r', encondig="UF-8")
   for line in file:
     print(line)

    
user_input = ""

while user_input !="exit":
    menu()
    user_input = input()
    if user_input == "1":
        read_file('aries.txt')
    elif user_input == "2":
        read_file("taurus.txt")
    elif user_input == "3":
      read_file("cancer.txt")
    elif user_input == "4":
      read_file("gemini.txt")
    elif user_input == "5":
      read_file("leo.txt")
    elif user_input == "6":
      read_file("virgo.txt")
    elif user_input == "7":
        read_file("libra.txt")
    elif user_input == "8":
      read_file("scorpio.txt")
    elif user_input == "9":
      read_file("sagittarius.txt")
    elif user_input == "10":
      read_file("capricornio.txt")
    elif user_input == "11":
      read_file("aquarius.txt")
    elif user_input == "12":
      read_file ("pisces.txt")
    elif user_input == "exit":
        print ("goodbye")
        exit ()
    else:
        print("opcion incorrecta")