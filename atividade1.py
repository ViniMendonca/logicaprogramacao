def calcula_soma(lista):
    lista = [2,4,6,8,10]
    return lista

lista = calcula_soma([2,4,6,8,10])
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(soma)


def converte_entrada(texto):
  texto = "2 8 0 5"
  lista_formatada = (texto.split(" "))
  for num in lista_formatada:
    num = int(num)
    lista_formatada.append(num)
    return lista_formatada
  
  
def processar_numeros(lista):
  lista = [2, 4, 6, 8]
  soma = 0
  i = 0
  for num in lista:
    soma+=num
    i += 1
  return (soma,i)


def main():
  entrada = input()
  lista=entrada.split(" ")
  soma = 0 
  for num in lista:
    soma += int(num)
  media = soma/len(lista)
  return media

  retorno = main()
  print(retorno)
  
  # essa atividade me fez refletir sobre a morte kkkkkkkkkkkk
 
    
    
    
