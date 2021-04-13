def exercicio1():
   lista = []
   soma = 0
   while len(lista) < 3:
     lista.append(int(input("insira a nota do aluno: ") ))
   for number in list:
     soma += number
   média = soma / 3
   return (f"média das notas é: {media}")
  
exercicio1()
   
#--------------------------------------------
  
  
def exercicio2(N):
  lista = []
  while len(lista) < N:
    lista.append(input(f"{len(lista) + 1} numero: "))
  return lista

exercicio()

#-------------------------------------------
                              
  def exercicio3():
    entrada = input("INSIRA a, b, z: ")
    if (entrada == 'z' or entrada == 'Z'):
     return
    elif (entrada == 'a'):
     print("globo")
    elif (entrada == 'b'):
     print('sbt')
    else:
      print('inválido')

#------------------------------------                            
                               
def exercicio4(list):
  medias_Inferiores_a_Sete = 0
  for media in list:
    if (media < 7):
      medias_Inferiores_a_Sete += 1
  if (medias_Inferiores_a_Sete
      < (len(list) * 0.25)):
    return "Professor Coxa"
  else:
    return "Professor Padrão"
