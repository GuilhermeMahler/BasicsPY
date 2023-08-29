#concatenação de Strings (juntar Strings)
#youtuber = "Guilherme Mahler"
#Formas de fazer isso

#Forma 1: 
#print("Se inscreva no" + youtuber)

#Forma 2:
#print("Se inscreva no{}".format(youtuber))

#Forma 3:
#print(f"Se inscreva no {youtuber}")

adj = input("Adjetivo:")
verb1 = input("Verbo1:")
verb2 = input("Verbo2:")
pessoa = input("Pessoa:")

madLib = print(f"Programacao no computador eh tao {adj}! Me deixa tao feliz o tempo todo porque \
 eu amo {verb1}. Se mantenha hidratado e {verb2} e voce eh {pessoa}!")

print(madLib)