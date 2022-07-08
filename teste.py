texto = list("quero um cachorro um quente umu") ### depois importar texto do arquivo

texto_a_deletar = list("um") ###input("Digite o texto a ser deletado: ")

i = 0

while i < len(texto):
    if texto_a_deletar[0] == texto[i]:
        print(i, " and ", texto[i])
        for x in range(i, i + len(texto_a_deletar) - 1):
            print(i, "aqui é o i e depois é o i + len", i + len(texto_a_deletar) - 1)
            y = 0
            if texto_a_deletar[y] == texto[x]:
                print("é igual e y={} e x={}".format(y, x))
            print(x, "é o X")
            y += 1
    print(i)
    i += 1

print(texto)
