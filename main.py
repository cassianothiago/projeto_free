import xmltodict #ler arquivo xml e traduzir para dicionario
import os #manusear arquivos 


def pegar_infos(nome_arquivo):
    with open(f'nfs/{nome_arquivo}','rb') as arquivo_xml: #abrir arquivo em python #armzenando o arquivo na viavel arquivo_xml
        dic_arquivo=xmltodict.parse(arquivo_xml) #transformar xml em dicionario python
        print(dic_arquivo)
        
lista_arquivos=os.listdir('nfs') #listar os arquivos de um diretorio(pasta)

for arquivo in lista_arquivos: #para cada arquivo em lista_arquivos pegar os arquivos
    pegar_infos(arquivo)
    break