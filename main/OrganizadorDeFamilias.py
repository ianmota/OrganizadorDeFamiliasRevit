import os
import shutil
import time

#Movimentações com os caminhos
caminho = 'G:\\Meu Drive\\2. Coordenador BIM\\Famílias\\Telefonia\\Desorganizado'
arquivos = os.listdir(caminho)

#Elementos de telefonia
ele = ['Tomada','Caixa','Campainha','Ponto de força','Sensor','Condulete','Poste','Quadro',
       'Medidor', 'Interruptor', 'Curva', 'Luminária', 'Suporte', 'Câmera', 'Tecla', 'Fiação',
       'Luva', 'Dobra', 'Conduíte', 'Unifilar', 'Módulo', 'Disjuntor'
    ]


for arquivo in arquivos:

    for i in range(len(ele)):
        if str.upper(ele[i]) in str.upper(arquivo):
            dire_dst = os.path.join(caminho,ele[i])
            dire_src = os.path.join(caminho,arquivo)
                
            if not os.path.isdir(dire_dst):
                    os.mkdir(dire_dst)
                
            shutil.move(dire_src,dire_dst)
            break

#Tempo decorrido        

print(time.process_time())