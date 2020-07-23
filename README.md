# Embrapii--Covid19
Repositorio destinado ao Processo Seletivo da Embrapii

## Para Rodar a Aplicação

Primeiro certifique-se que você possui o Docker e o Docker Compose instalado no seu computador.

### Certificando
Docker
```
sudo docker --version
```

Docker-Compose
```
sudo docker-compose --version
```

Se nos dois aparecer a versão, significa que está tudo certo e você pode prosseguir no processo de rodar o projeto.
Caso constrário, acesse os links para instalar o [Docker](https://docs.docker.com/install/) e o [Docker-Compose](https://docs.docker.com/compose/install/).

- Faça as migrações pelo comando

  `sudo docker-compose run web python manage.py makemigrations`

- Aplique as migrações pelo comando

  `sudo docker-compose run web python manage.py migrate`

### Rodando Aplicação

  - Após a realização de todos os passos suba a aplicação pelo comando

  `sudo docker-compose up`
  
### Detalhes 
  
  As rotas do projeto são:
  
  - "/patients" - destinada a Criar e Listar de elementos;
  - "/patients-edit" - destinada a Editar e Deletar os elementos;
  

