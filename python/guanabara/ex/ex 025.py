'''
Crie um programa que leia o nome de uma  pessoa e diga se ela tem 'Silva' no nome
'''

nome = input('Digite seu nome: ').strip().title() +' '
print('no nome {} tem "Silva"?\n{}'.format(nome, 'Silva ' in nome))