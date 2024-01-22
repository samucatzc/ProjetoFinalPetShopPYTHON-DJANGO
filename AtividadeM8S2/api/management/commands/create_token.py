from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import User
class Command(BaseCommand):
     def add_arguments(self, parser):
          parser.add_argument('--username', required=True)
          parser.add_argument('--password', required=True)

     def handle(self, *args, **options):
          username = options['username']
          password = options['password']
          self.stdout.write(
               self.style.WARNING(f'Criando Usuário com o nome {username}')
          )
          user = User(username=username)
          user.first_name = username
          user.set_password(password)
          user.save()
          self.stdout.write(
               self.style.SUCCESS('Usuario criado')
          )
          self.stdout.write(
               self.style.WARNING('Criando token para usuario')
          )
          token = Token.objects.create(user=user)
          self.stdout.write(
               self.style.SUCCESS(f'Token criado para o usuário {token.key}')
          )
     