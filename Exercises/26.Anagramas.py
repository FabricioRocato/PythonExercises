def verificar_anagrama(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    # Ordenar as letras das strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if verificar_anagrama(string1, string2):
    print("As strings são anagramas.")
else:
    print("As strings não são anagramas.")
