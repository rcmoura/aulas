nome = input("Entre com o nome do Aluno: ")
nota1 = float(input("Entre com a 1a. Nota: "))
nota2 = float(input("Entre com a 2a. Nota: "))
media = (nota1 + nota2)/2;
if media >= 7 :
     print("Nome: ",nome," - Média-> ",media," -> Aprovado")
else :
    if media <= 3 :
         print("Nome: ",nome," - Média-> ",media," -> Retido")
    else :
         print("Nome: ",nome," - Média-> ",media," -> Prova Final")