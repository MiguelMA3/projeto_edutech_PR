# v = deslocamento
#     ____________
#        tempo

vel = float(input('Qual a velocidade(m/s)? '))
print(f'Velocidade: {vel} m/s = {vel*3.6}\n')
distancia = float(input('Qual a distância(m)? '))
print(f'Distância: {distancia} m = {distancia*1000}\n')

print('Calculando tempo...')
tempo = distancia / vel

print(f'Tempo de viagem = {tempo:.2f} Segundos - ou - {tempo/60:.2f} Minutos')
