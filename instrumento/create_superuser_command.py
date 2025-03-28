from django.core.management.base import BaseCommand
from instrumento.models import Cliente

class Command(BaseCommand):
    help = 'Cria um superusuário se ele não existir'

    def handle(self, *args, **options):
        if not Cliente.objects.filter(is_superuser=True).exists():
            Cliente.objects.create_superuser(
                email='bragasan34@gmail.com',
                password='101219',
                nome='Francisco Santana',
                cpf='49322893249'
            )
            self.stdout.write(self.style.SUCCESS('Superusuário criado com sucesso!'))
        else:
            self.stdout.write(self.style.SUCCESS('Superusuário já existe.'))
