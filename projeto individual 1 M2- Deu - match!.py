################################################################
##   Aluna: Ana Paula Ferreira                                ##
##   Curso: Formação Análise de Dados                         ##
##   Instituição: Senac                                       ##
##   Metodologia : Resilia                                    ##
##   Projeto 1 Módulo 2 : Deu match!                          ## 
################################################################


import pandas as pd  #importando a biblioteca panda
lista = [] 
def ficha():
    
    s=" "
    lista2=[]
    while True: #estrutura de reptição para adicionar os cadidatos e as nota, e convertendo as as notas para a str 
        nome = input('Nome do candidato: ')
        nota1 = float(input('Digite a nota da entrevista: '))
        nota2 = float(input('Digite a nota do teste teorico: ')) 
        nota3 = float(input('Digite a nota teste pratico: ')) 
        nota4 = float(input('Digite a nota do softskill: '))
        lista_candidato = [nome, nota1, nota2,nota3,nota4]
        lista.append(lista_candidato)
        s="e"+str(nota1)+"_"+"t"+str(nota2)+"_"+"p"+str(nota3)+"_"+"s"+str(nota4) # convertendo as as notas para a str no formato que o texto pede  
        print(nome,"obteve as notas:",s)
        lista2.append([nome,s])
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
        print('-'*70)
        if cont == 'N':
            break


    return pd.DataFrame(lista2, columns=["CANDIDATOS","RESULTADO"]) #criando a coluna e inserindo lista2 na coluna 

print('-'*70)


def imprime(lista): #imprenção da lista
 for i in lista:
    print(i)


def buscar(e,t,p,s): #funçaõ para buscar os candidatos e notas
  usuarios=[]
  for candidato in lista:
      usuario=[]
      nome=candidato[0]
      if (float(e)<= candidato[1]) and (float(t)<= candidato[2]) and (float(p)<= candidato[3]) and (float(s)<= candidato[4]):
        usuario.append(nome)
        usuario.append([candidato[1],candidato[2],candidato[3],candidato[4]])
      usuarios.append(usuario)
  for i in usuarios:
    if i == []:
      usuarios.remove(i) #removendo os indice que vazio no código
  return imprime(usuarios)

print(ficha())# aqui precisamos chamar a a def para rodar o código 
print(buscar(7,5,6,8)) #aqui precisa digitar as notas que deseja buscar