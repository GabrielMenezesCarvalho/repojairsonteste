from django.db import models

class Horarios(models.Model):
    horarioDeAbertura = models.TimeField()
    horarioDeFechamento = models.TimeField()

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return f"Horario de Abertura {self.horarioDeAbertura} {self.horarioDeFechamento}"

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, null=True)
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        #senha tem que ver o jeito seguro de armazenar, XD
        return f"Usuário {self.nome } {self.email}  {self.telefone}" 
  

class Restaurantes(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    capacidadeDeMesas = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'

    def __str__(self):
        return f"Restaurante {self.nome} {self.endereco} {self.capacidadeDeMesas}"
    
class Mesa(models.Model):
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE)
    numeroDaMesa = models.CharField(max_length=100)
    capacidadeDaMesa = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"Mesa {self.numeroDaMesa} {self.capacidadeDaMesa}"

class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    restaurante = models.ForeignKey(Restaurantes, on_delete=models.CASCADE, null=True)

    dataDaReserva = models.DateField()
    horaDaReserva = models.TimeField()
    numero_de_pessoas = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"Reserva para {self.usuario} em {self.dataDaReserva} às {self.horaDaReserva}"


