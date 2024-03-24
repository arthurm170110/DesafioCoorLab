# Resultado - Desáfio CoorLab

# Backend
  Primeiramente foi criado uma API REST com o auxílio do framework Django e e utizando a linguagem Python, onde a partir do arquivo json fornecido eu populo o banco de dados e sempre que for adicionado novas cotações de viagem no arquivo json meu banco é atualizado, foi utilizado o SQLite, padrão do Django, mas podendo ser alterado para qualquer outro. Nesta API possui apenas duas rotas:
  - transport/ , onde é feito um GET em todas as cotações
  - transport/city/cidade_exemplo/ , que para cada cidade retorna a viagem mais econômica e a mais rápida e confortável

# Frontend
  Para o frontend foi utilizado o Vue 3 e foi criado tentando seguir ao máximo o exemplo fornecido. Cada componente que eu julgava necessário era criado e adicionado a view HomeView.vue e em seguido ela foi adicionada no App.vue onde tudo é executado.

  Para o run.sh rodar, estou considerando que será executado da seguinte forma: ./run.sh &
