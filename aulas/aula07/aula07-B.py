vel = input("Velocidade do veículo em km/h: ")      #input


if vel <= 0 or vel > 500:                                 #+------detetor de negativos ou valores superiores ao limite
        print("Erro: Velocidade inválida")                #+


else:
    if vel > 80:                                                  #+                        #+
        a = vel - 80                                              #|                        #|
        t = a                                                     #+---calculador da multa  #|
        a = round(t, 2)                                           #|                        #|
        print(f"Passou o limite! Agora terá de pagar {a} euros.") #+                        #+-------detetor de crime
                                                                                            #|
    elif vel <= 80:                                                                         #|
        print("não passou o limite :D pode continuar a conduzir ;)")                        #+

