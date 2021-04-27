restaurantes = []

informacoes = ["A Feijoada",4.4,9.90]
restaurantes.append(informacoes)

informacoes = ["Makis Place - Saúde",4.7,7.99]
restaurantes.append(informacoes)

informacoes = ["Sukiya - Saúde",4.6,7.99]
restaurantes.append(informacoes)

informacoes = ["Viena - Shopping Santa Cruz",4.4,12.49]
restaurantes.append(informacoes)

informacoes = ["Kibon Sorveteria - Saúde",4.9,6.99]
restaurantes.append(informacoes)

informacoes = ["Giraffas Carrefour Metrocar",4.4,5.99]
restaurantes.append(informacoes)

for i in range(1,len(restaurantes)) :
    posicao = restaurantes[i]
    j=i-1
    while  j>=0 and posicao[1]>=restaurantes[j][1] :
        if posicao[1]>restaurantes[j][1] :
            restaurantes[j+1] = restaurantes[j]
            j=j-1
        if posicao[1]==restaurantes[j][1] :
            if posicao[2]<restaurantes[j][2] :
                   restaurantes[j+1] = restaurantes[j]
                   j=j-1
            else :
                break
    restaurantes[j+1] = posicao
    
print(restaurantes)
