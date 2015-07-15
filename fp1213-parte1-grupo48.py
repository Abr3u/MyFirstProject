#Ricardo Jorge Lopes de Abreu, 76370; Rui Miguel Hungria Furtado, 76379; Alex Novella Bitton Ferreira, 76465

from NASA import *

valores=[]
desconhecidos=[]
def temperatura(x,y):
    global valores
    global desconhecidos
    if isinstance(conteudo(x,y),float):
        t = conteudo(x,y)
        return t, desconhecidos
    else: #neste caso a temperatura não está definidada na função conteudo
        vizinhanca = [(x-1,y+1),(x,y+1),(x+1,y+1),(x-1,y),(x+1,y),(x-1,y-1),(x,y-1),(x+1,y-1)]
        numerador=0
        denominador=0        
        for el in range(len(vizinhanca)):
            for el2 in range(len(vizinhanca[1])):
                if isinstance(conteudo(el,el2),float):
                    numerador=numerador+conteudo(el,el2)
                    denominador=denominador+1
                    t=numerador/denominador
        if denominador==0: #neste caso os números à volta deste ponto também não têm temperaturas definidas na função conteudo
            t=valores[len(valores)-1] #temperatura assume a temperatura do ponto anterior
        desconhecidos = desconhecidos+ [((x,y),t)]
    return t, desconhecidos

def caminho (x,y):
    global valores
    global desconhecidos    
    soma = 0
    if x==dimensoes()[0]/2: #dimensoes()[0]/2 corresponde à coluna do meio do mapa
        valores = [temperatura(x,y)[0]]
    elif x > dimensoes()[0]/2: 
        while x != (dimensoes()[0]/2) - 1: #é necessário retirar uma unidade para ainda ser calculada a temperatura no ponto dimensoes()[0]/2
            valores = valores + [temperatura(x,y)[0]]
            x = x-1
        x=x+1 #dá-se o acerto da coordenada x, para esta voltar a ser dimensoes()[0]/2
            
    else:
        while x != (dimensoes()[0]/2) + 1: 
            valores = valores + [temperatura(x,y)[0]]
            x = x+1
        x=x-1
            
    if y <= (dimensoes()[1]/2): #dimensoes()[1]/2 corresponde à linha do meio do mapa
        while y != (dimensoes()[1]) + 1: #é necessário acrescentar uma unidade para ser calculada a temperatura na posição fronteira (neste caso dimensoes()[1])
            valores = valores + [temperatura(x,y)[0]]
            y = y+1
        y=y-1 #dá-se o acerto da coordenada y, para esta voltar a ser dimensoes()[1]
            
    else:
        while y != -1: #é necessário retirar uma unidade para que seja calculada a temperatura na posição fronteira (neste caso 0)
            valores = valores + [temperatura(x,y)[0]]
            y = y-1
        y=y+1 #dá-se o acerto da coordenada y, para esta voltar a ser 0
            
    for i in valores:
        soma = soma + i #somar todas as temperaturas calculadas nos pontos
    valor_medio = soma / len(valores) #dividir soma pelo número de elementos somados - média aritmética
    return valor_medio, y

def temperaturas(x,y):  
    global valores
    global desconhecidos
    valores=[]
    desconhecidos=[]
    return [(x,y), (dimensoes()[0]/2,y), (dimensoes()[0]/2,caminho(x,y)[1]), (caminho(x,y)[0]), (temperatura(x,y)[1])]