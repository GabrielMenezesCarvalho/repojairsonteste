import os
import django
import random
from faker import Faker
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seu_projeto.settings")
django.setup()

from seu_app.models import Horarios, Usuarios, Restaurantes, Mesa, Reserva

fake = Faker("pt_BR")

def populate_horarios(num_entries=5):
    for _ in range(num_entries):
        horario = Horarios.objects.create(
            horarioDeAbertura=fake.time(),
            horarioDeFechamento=fake.time()
        )
        print(f"Horário criado: {horario}")

def populate_usuarios(num_entries=50):
    for _ in range(num_entries):
        usuario = Usuarios.objects.create(
            nome=fake.name(),
            email=fake.email(),
            senha=fake.password(),
            telefone=fake.phone_number()
        )
        print(f"Usuário criado: {usuario}")

def populate_restaurantes(num_entries=10):
    for _ in range(num_entries):
        restaurante = Restaurantes.objects.create(
            nome=fake.company(),
            endereco=fake.address(),
            capacidadeDeMesas=random.randint(10, 50)
        )
        print(f"Restaurante criado: {restaurante}")

def populate_mesas():
    restaurantes = Restaurantes.objects.all()
    for restaurante in restaurantes:
        num_mesas = random.randint(5, restaurante.capacidadeDeMesas)
        for i in range(num_mesas):
            mesa = Mesa.objects.create(
                restaurante=restaurante,
                numeroDaMesa=f"Mesa {i + 1}",
                capacidadeDaMesa=random.randint(2, 8)
            )
            print(f"Mesa criada: {mesa}")

def populate_reservas(num_entries=100):
    mesas = Mesa.objects.all()
    usuarios = Usuarios.objects.all()
    for _ in range(num_entries):
        mesa = random.choice(mesas)
        usuario = random.choice(usuarios)
        reserva = Reserva.objects.create(
            mesa=mesa,
            usuario=usuario,
            restaurante=mesa.restaurante,
            dataDaReserva=fake.date_between(start_date='-1y', end_date='today'),
            horaDaReserva=fake.time(),
            numero_de_pessoas=random.randint(1, mesa.capacidadeDaMesa)
        )
        print(f"Reserva criada: {reserva}")

def run():
    print("Populando horários...")
    populate_horarios()
    print("Populando usuários...")
    populate_usuarios()
    print("Populando restaurantes...")
    populate_restaurantes()
    print("Populando mesas...")
    populate_mesas()
    print("Populando reservas...")
    populate_reservas()
    print("População completa!")

if __name__ == '__main__':
    run()
