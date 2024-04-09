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

# 3-atualizar/cosulta

# 4-delete delete()
# 5-consultar 1 registro get()
# 6-consultar 5 diferentes
