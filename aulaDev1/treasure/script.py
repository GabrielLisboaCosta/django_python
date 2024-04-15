from exemplo.models.exemplo import Example
from django.contrib.auth import get_user_model
from random import randint

User = get_user_model()

opcao = input("Escolha a opção que deseja: ")

# 1-gerar dados save()
if opcao == 1:
    times = ["Flamengo", "Palmeiras", "Corinthians", "Santos", "Cruzeiro", "Atlético Mineiro", "Brasil de Pelotas",
             "Avaí", "São Paulo", "Fluminense", "Chapecoense", "Juventude", "Caxias"]

    for time in times:
        add_time = Example(nome=time, torcedores=randint(1, 10000))
        add_time.save()

# 2-criar super usuario
elif opcao == 2:
    User.objects.create_superuser('ifrs', 'admin@myproject.com', 'ifrs2023')
    print("User: ifrs / Senha: ifrs2023")

# 3-atualizar/consulta
elif opcao == 3:
    flamengo = Example.objects.get(nome="Flamengo")
    flamengo.torcedores = randint(1, 10000)  # Atualiza o número de torcedores
    flamengo.save()  # Salva as alterações

    todos_times = Example.objects.all()
    for time in todos_times:
        print(f"Time: {time.nome}, Torcedores: {time.torcedores}")

# 4-delete delete()
# elif opcao == 4:
#    cruzeiro = Example.objects.get(nome="Cruzeiro")
#    cruzeiro.delete()

# 5-consultar 1 registro get()
elif opcao == 5:
    palmeiras = Example.objects.get(nome="Palmeiras")
    print(f"Time: {palmeiras.nome}, Torcedores: {palmeiras.torcedores}")

# 6-consultar 5 diferentes
elif opcao == 6:
    import random
    random_times = random.sample(Example.objects.all(), 5)
    for time in random_times:
        print(f"Time: {time.nome}, Torcedores: {time.torcedores}")
