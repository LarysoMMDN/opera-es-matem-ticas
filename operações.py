limpar = '\033[m'
blue = '\033[1;34m'
rosa = '\033[1;35m'
red = '\033[1;31m'
igual = ('='*15)

repetição = True

print(f'{rosa}{igual}OPERAÇÕES MATEMÁTICAS{igual}{limpar}')
print(f'{blue}bom, este programa foi criado para ajudar você a resolver problemas matemáticos{limpar}')
confirmação = input(f'{blue}vamos começar?{limpar} ')
if confirmação == 'sim':
    selecione = input(f'{blue}bom qual é o operador matemático que voce vai usar? {limpar}\nescolha:{red}\nmultiplicação\nadição\nsubtração\ndivisão\n{limpar}')
    print(f'{rosa}{igual}{igual}{igual}{limpar}')
    if selecione == 'multiplicação':
        while repetição:
            num_m1 = float(input(f'{blue}okay, me diga o primeiro digito da sua multiplicação :{limpar} '))
            num_m2 = float(input(f'{blue}bom, agora me de o segundo digito da operação :{limpar} '))
            result_m = num_m1 * num_m2
            print(f'{rosa}bom, a multiplicação entre {num_m1} e {num_m2} é igual a {result_m:.2f}{limpar}.')
            replay_m = input(f'{blue}vai querer fazer outra operação de multiplicação?{limpar} ')
            if replay_m == 'sim':
                repetição = True
            else:
                print(f'{rosa}okay, espero ter ajudado =){limpar}')
                repetição = False
    elif selecione == 'adição':
        while repetição:
            num_a1 = float(input(f'{blue}bem, me diga o primeiro numeroda sua adição :{limpar} '))
            num_a2 = float(input(f'{blue}okay, me diga o segundo numero da sua adição :{limpar} '))
            result_a = num_a1 + num_a2 
            print(f'{rosa}bom a soma entre {num_a1} e {num_a2} é igual a {result_a:.2f}{limpar}.')
            replay_a = input(f'{blue}bem, vai querer outra operação de adição?{limpar} ')
            if replay_a == 'sim':
                repetição = True
            else:
                print(f'{rosa}okay, espero ter te ajudado :){limpar}')
                repetição = False
    elif selecione == 'subtração':
        while repetição:
            num_s1 = float(input(f'{blue}tudo bem!, me diga o primeiro numero da sua subtração :{limpar} '))
            num_s2 = float(input(f'{blue}okay, me diga o segundo número da subtração :{limpar} '))
            result_s = num_s1 - num_s2
            print(f'{rosa}bem, a sutração entre {num_s1} e {num_s2} é igual a {result_s:.2f}{limpar}.')
            replay_s = input(f'{blue}okay, vai querer fazer outra operação?{limpar} ')
            if replay_s =='sim':
                repetição = True
            else:
                print(f'{rosa}tudo bem, te agradeço por usar meu programa =){limpar}')
                repetição = False
    elif selecione == 'divisão':
        while repetição:
            num_d1 = float(input(f'{blue}ok, me diga o primeiro numero da sua divisão :{limpar} '))
            num_d2 = float(input(f'{blue}beleza, me diga o segundo numero da divisão :{limpar} '))
            result_d = num_d1 / num_d2
            print(f'{rosa}okay, a divisão entre {num_d1} e {num_d2} é igual a {result_d:.2f}{limpar}.')
            replay_d = input(f'{blue}bom, vai querer fazer outra divisão?{limpar} ')
            if replay_d =='sim':
                repetição = True
            else:
                print(f'{blue}okay, muito obrigado por usar esse programa :){limpar}')
                repetição = False
    else:
        print(f'{red}ops!,talvez você tenha escrito o nome do operador errado, você terá que reiniciar o código :|{limpar}')              
else:
    print(f'{red}okay, parece que voce não quer usar o programa ou voce escreveu errado a palavra "sim"{limpar}.')      