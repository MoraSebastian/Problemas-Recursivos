
from random import sample

def generarMazo():
	return sample([(x,y) for x in ['A','2','3','4','5','6','7','8','9','10','J','Q','K'] for y in ['picas','treboles','corazones','diamantes']],52)

def determinarGanador(jugador,casa):
        print 'se determino el ganador'
        if validacionDeVentiUna(casa)>=validacionDeVentiUna(jugador):
                print 'Gano la casa'
        else:
                print 'Gano el jugador'


def validacionDeVentiUna(mazo):
    print contarMazo(mazo,0,11)
    return contarMazo(mazo,0,11)


def buscarAs(mazo):
  if len(mazo)==0:
    return False
  else:
    if min(mazo[0])=='A':
      return True
    else:
      return buscarAs(mazo[1:])
      
def contarMaz(mazo):
  
  if len(mazo)==0:
    return 0 
  else:
    return obtenerValor(min(mazo[0]))+contarMaz(mazo[1:])


def validarAs(mazo):
  if contarMaz(mazo)<=11 and buscarAs(mazo):
      return contarMaz(mazo)+10
  else:
      return contarMaz(mazo)
  
def obtenerValor(valor):

    if valor =='A':
        return 1
    if valor =='2':
        return 2
    if valor =='3':
         return 3
    if valor =='4':
        return 4
    if valor =='5':
        return 5
    if valor =='6':
        return 6
    if valor =='7':
        return 7
    if valor =='8':
        return 8
    if valor =='9':
        return 9
    if valor =='10':
        return 10
    if valor =='J':
        return 10
    if valor =='Q':
        return 10
    if valor =='K':
        return 10
    else:
        return 0

def jugar(mazo,jugador,casa,momento):
    if momento ==0:
        if len(mazo) >=2:
            return jugar(mazo[4:],jugador+[mazo[0]]+[mazo[2]],casa+[mazo[1]]+[mazo[3]],1)
        else:
          print mazo
    if momento ==1:
        print validarAs(jugador)
        print jugador[1:],"carta oculta", jugador[0]
        print casa[1:],"carta oculta", casa[0]
        if input("1 para mas cartas \n2 para parar\n") ==1 :
            return jugar(mazo[1:], jugador + [mazo[0]], casa , 1)
        else:
            return jugar(mazo, jugador, casa, 2)
    if momento ==2:
        print jugador[1:],"carta oculta", jugador[0]
        print casa[1:],"carta oculta", casa[0]
        if input("1 para mas cartas \n2 para parar\n") ==1 :
            return jugar(mazo[1:], jugador, casa + [mazo[0]] , 2)
        else:
            return jugar(mazo, jugador , casa, 3)
    if momento ==3:
        determinarGanador(jugador,casa)

jugar(generarMazo(),[],[],0)
