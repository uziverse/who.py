
aa = ""
print(aa)
print("\033[1;91m o script precisa da lib whois e python whois")
print(" \033[1;91mpara add ; pip3 install whois , pip3  install python-whois")

import whois

def menu():
    print("\033[1;34m")
    print("*"*30)
    print("{:^30}".format("\033[1;34m script total scan 1.0 by uzi"))
    print(aa)
    print("{:^25}".format("\033[1;34m para encerrar, ctrl + c"))
    print("*"*30)
    print(aa)
    return None

while True:
    menu()
    dominio = input("\033[1;32msite/ip: ")
    consult = whois.whois(dominio)

    print(consult)
    print(aa)
    salvar = input("\033[1;95m deseja salvar o resultado? y = SIM n = NÃO: ")
    print(aa)
    if salvar == "y":
        arquivo = open('arq.txt','w')
        arquivo.write(str(consult))
        arquivo.close()
        print(" arquivo salvado com sucesso em cima do arquivo antigo se existia, nome : arq.txt")
        
    else:
        continue
    