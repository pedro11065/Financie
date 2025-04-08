opcoes = {

    'nrs': 
    {    
        1: '8',
        # 2: '11',
        # 3: '12',
        # 4: '13',
        # 5: '33',
        # 6: '35'
    },

    'nr-8':

    {
        1: 'rampa',
        2: 'escada_com_espelho',
        3: 'escada_sem_espelho',
        4: 'passarela_plana',
        5: 'passarela_inclinada',
        6: 'guarda_corpo'
    }

}

print('qual nr deseja analisar?')
for i, nr in opcoes['nrs'].items():
    print(f'{i} - nr {nr}')

escolha_nr = int(input('\ndigite o numero da nr: '))

if escolha_nr in opcoes:  print('opcao invalida'); exit()
nr = opcoes['nrs'][escolha_nr]; nr_str = 'nr-' + nr

#-------------------------------------------------------------

print(f'\n\nqual tipo de equipamento que deseja analisar?')
for i, tipo in opcoes[nr_str].items():
    print(f'{i} - {tipo.replace("_", " ")}')

escolha_tipo = int(input('\ndigite o numero do tipo: '))

if escolha_tipo not in opcoes[nr_str]:  print('opcao invalida'); exit()
tipo = opcoes[nr_str][escolha_tipo]

#-------------------------------------------------------------


print(f'\n\nvoce escolheu o nr {nr} e o tipo {tipo.replace("_", " ")}\n\n')







