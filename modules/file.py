#retorna uma lista com o conteúdo do arquivo separado por linha
def line_content(arquivo):
    content = arquivo.read()
    content_list = content.split("\n")

    return content_list

#escreve os dados de uma lista no arquivo
def write_file(arquivo, lista, tam):

    for x in range (tam):
        arquivo.write(f"{lista[x]}\n")
       