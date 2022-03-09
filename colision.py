from modules.file import * #importando as funções do módulo
#================CLI=========================================#
import argparse

#instruções:
# -s = score
# -c = clear score
# -b = best score
# -w = worst score

#Configurando os argumentos
parse = argparse.ArgumentParser("Colision-Game")
parse.add_argument("-s","--score", help="get all scores(highest five scores)", action="store_true")
parse.add_argument("-c","--clear", help="clear all scores", action="store_true")
parse.add_argument("-b","--best",help="get the best score", action="store_true")
parse.add_argument("-w","--worst",help="get the worst score", action="store_true")
args = parse.parse_args()

#Captando o conteúdo do arquivo
with open("./data/score.txt","r") as score:
    content = line_content(score)
    content.pop() #removendo uma string vazia do final da lista

#Tratando os argumentos
if args.score:
    
    if len(content) == False:  #Caso não haja conteúdo no arquivo
        print("Void score. Play the game!")
    else:
        count = 1
        for placar in content:  #imprimindo o rank
            print(f"{count}º -> {placar}")
            count += 1

elif args.clear:
    with open("./data/score.txt","w") as score:
        score.write("") #limpando o arquivo

elif args.best:
    print(f"Best score -> {min(content)}") #pega menor valor

elif args.worst:
    print(f"Worst score -> {max(content)}") #pega maior valor

else:
    import modules.game #rodando o game
    
    #=======================FORMATAÇÃO DO ARQUIVO SCORE======================#
    time = modules.game.result_time

    print(f"Your score = {round(time,2)}")

    with open("./data/score.txt","a") as score:
        score.write(f"{round(time,2)}")

    with open("./data/score.txt","r") as score:
        c_lines = line_content(score)

    c_lines.sort()
    if len(c_lines) > 5:
        c_lines.pop()

    with open("./data/score.txt","w") as score:
        write_file(score,c_lines,len(c_lines))
