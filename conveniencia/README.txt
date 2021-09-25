# Instruções para executar a API:

1 - Abra o projeto em seu ambiente de desenvolvimento;
2 - Abra o terminal e vá até o diretório conveniencia;
3 - Execute o comando python manage.py runserver para rodar a aplicação (A porta padrão é :8000);
4 - Após ter executado o 3º passo, abra seu navegador e acesse: http://localhost:8000
5 - Caso tudo tenha ocorrido bem, o servidor retornará a página com o end-point criado para a api Purchases

# Instruções extras

1 - É necessário ter o Python instalado em sua máquina (É recomendado que se instale a última versão do Python 3 - https://docs.djangoproject.com/pt-br/3.2/faq/install/#faq-python-version-support);
2 - É necessário ter o Django instalado em sua máquina, caso não o possua, tente executar o comando python -m pip install Django, caso retorne algum erro, verifique se o pip está instalado em sua máquina.
(Windows - py -m pip --version / Linux - python -m pip --version / MacOS - python -m pip --version)
3 - Caso queira acessar a página de admin do django para incluir dados nos campos, execute dentro do diretorio raíz do projeto o comando python manage.py createsuperuser e com o servidor em execução vá até: http://localhost/admin
