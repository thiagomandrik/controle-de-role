def bemvindo():
    print ('')
    print ('#################################################')
    print ('#                                               #')
    print ('# Seja bem vindo ao Sistema de Controle de Rolê #')
    print ('#                                           1.0 #')
    print ('#################################################')
    print ('')
def prog():
    participantes = int(input("Quantas pessoas irão participar desse rolê mitológico? "))
    compraram = int(input("Quantas pessoas compraram as coisas? "))
    cont = 1
    valores = []
    while cont <= compraram:
        valores.append(float(input("Valor pago pela pessoa %i°: " %cont)))
        cont+=1
    valor = 0

    for i in valores:
        valor = float(i) + float(valor)
    valor = float(valor/participantes)
    print('Cada um vai pagar R$%.2f pelo rolê mitológico!' %valor)



bemvindo()
prog()
