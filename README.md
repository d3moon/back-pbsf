
# Backend - Desafio PBSF

Essa aplicação destina-se à criação de uma API em Python usando Django Rest Framework que tem como objetivo manipular uma aplicação de Vacinas. 

**As funcionalidades da API são:**

- Criar Vacinas;
- Atualizar Vacinas
- Deletar Vacinas;
- Listar Vacinas;
- Possui logs de execução;
- Possui persistência com o banco de dados SQLite;



## Instalação

Instale e rode o projeto com:

```bash
  cd back-pbsf
  python3 -m virtualenv venv
  source venv/bin/activate  
  pip install -r requirements.txt
  python3 manage.py runserver
```

## Referência de API

| Rota      | Método | Descrição |
| ----------- | ----------- | ----------- |
| /vacinas/     | POST     | Registrar Vacinas       |
| /vacinas/   | GET        |  Listar Vacinas       |
| /vacinas/   | PUT        |  Atualizar Vacinas       |
| /vacinas/   | DELETE        |  Deletar Vacinas       |


## Authors

- [João Victor F. Braga](https://www.github.com/d3moon)
- [LinkedIn](https://www.linkedin.com/in/d3moon)

# back-pbsf
