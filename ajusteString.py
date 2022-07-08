
### Main ###

texto = list("quero um unidos limão um") ### depois importar texto do arquivo

texto_a_deletar = "ro" ###input("Digite o texto a ser deletado: ")

i = 0
eh_igual = False

while i < len(texto):
    if texto_a_deletar[0] == texto[i]:
        ### verifica se sequência de caracteres do texto é igual ao texto que precisa ser buscado
        y = 0
        for x in range(i, i + len(texto_a_deletar)):            
            if texto_a_deletar[y] == texto[x]:
                eh_igual = True
                print(x)
                print("{} é igual a {}".format(texto[x], texto_a_deletar[y]))
            else:
                eh_igual = False
                print(x)
                print("caracter {} é diferente".format(texto[x]))
            y += 1
        if (eh_igual == True):
            for k in range(i, i + len(texto_a_deletar)):
                texto[k] = " "
    i += 1
      

print(texto_a_deletar)
print(texto)

### Funções ###

def carrega_texto():
    arquivo = open("texto.txt", "r", encoding = "utf-8")
    texto = []


##print(len(str))

##for lttr in str:
##    print("a letra é {}\n".format(lttr))