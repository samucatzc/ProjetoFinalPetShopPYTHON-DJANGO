from django import forms
from datetime import date
from base.models import Contato, Reserva, Agendamento, Categoria, Pet

class PetForm(forms.ModelForm):
   class Meta:
     model = Pet


     fields = ['nome', 'categoria']

     widgets = {
        'nome'  : forms.TextInput(
           attrs={
              'placeholder' : 'insira o nome do pet aqui'
           }   
        ),
        'categoria'  : forms.Select(
           choices = tuple(Categoria.objects.all()),
        ),
         }  
   labels = {
       'nome' : 'Nome: ',
       'categoria' : 'Categoria'
    }

class CategoriaForm(forms.ModelForm):
   class Meta:
     model = Categoria


     fields = ['tipo', 'tamanho']

     widgets = {
        'tipo'  : forms.TextInput(
           attrs={
              'placeholder' : 'insira o tipo aqui'
           }
        ),
        'tamanho' : forms.TextInput(
           attrs={
              'placeholder' : 'insira o tamanho aqui'
           }
        ),
        
           }  
   labels = {
       'tipo' : 'Tamanho:',
       'tamanho' : 'Tamanho:',
    }
class AgendamentoForm(forms.ModelForm):
   class Meta:
      model = Agendamento


      fields = "nome", "email", "nome_do_pet", "data", "observacoes"

      widgets = {
         'nome'   : forms.TextInput(
            attrs={
               'placerholder'  : 'insira o seu nome aqui'
            }
         ),
         'email' : forms.EmailInput(
            attrs={
               'placeholder' : 'insira o seu e-mail aqui'
            }
         ),
         'nome_do_pet'   : forms.TextInput(
            attrs={
               'placerholder'  : 'insira o nome do pet aqui'
            }
         ),
         'data'   : forms.TextInput(
            attrs={
               'placerholder'  : 'insira a data aqui'
            }
         ),
         'observações': forms.Textarea(
            attrs={
               'placeholder' : 'insira o sua mensagem aqui'
            }
         )
      }
   labels = {
      'nome' : 'Nome:',
      'email' : 'E-mail:',
      'nome_do_pet' : 'Nome Do Pet:',
      'data' : 'Data de Reserva',
      'observacoes' : 'obsevacoes'
   }
class ContatoForm(forms.ModelForm):
   class Meta:
     model = Contato


     fields = ['nome', 'email', 'mensagem']

     widgets = {
        'nome'  : forms.TextInput(
           attrs={
              'placeholder' : 'insira o seu nome aqui'
           }
        ),
        'email' : forms.EmailInput(
           attrs={
              'placeholder' : 'insira o seu e-mail aqui'
           }
        ),
        'mensagem': forms.Textarea(
           attrs={
              'placeholder' : 'insira o sua mensagem aqui'
           }
        )
      }
   labels = {
       'nome' : 'Nome:',
       'email' : 'E-mail:',
       'mensagem' : 'Mensagem'
    }

class ReservaForm(forms.ModelForm):
   class Meta:
     model = Reserva

     fields = ['nome_do_pet', 'telefone','data', 'mensagem', 'categoria']

     widgets = {
        'nome_do_pet'  : forms.TextInput(
           attrs={
              'placeholder' : 'insira o seu nome do seu pet aqui!'
           }
        ),
        'telefone' : forms.TextInput(
           attrs={
              'placeholder' : 'insira o seu telefone aqui!'
           }
           
        ),
        'data' : forms.DateInput(
            attrs={'type' : 'date'}
        ),
      

        'mensagem': forms.Textarea(
           attrs={
              'placeholder' : 'insira o sua mensagem aqui!'
           }
        )
      }
     labels = {
       'nome_do_pet' : 'Nome do Pet:',
       'telefone' : 'Telefone:',
       'data' : 'Data de Reserva',
       'mensagem' : 'Mensagem',
       'categoria' : 'Tamanho do Pet: '

    }

   def clean_data(self):
      data = self.cleaned_data['data']
      data_de_hoje = date.today()
      if data < data_de_hoje:
         raise forms.ValidationError('Você não pode reservar uma da ta do passado!!!')
      numero_reservas = Reserva.objects.filter(data=data).count()
      if numero_reservas >= 4:
         raise forms.ValidationError('Todas as reservas desse dia foram ocupadas!!!')
      return data