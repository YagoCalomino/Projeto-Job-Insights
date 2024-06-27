# Boas-vindas ao repositório do Job Insights!

Para realizar o projeto, atente-se a cada passo descrito a seguir, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir deste repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

# Termos e acordos

Ao iniciar este projeto, você concorda com as diretrizes do Código de Conduta e do Manual da Pessoa Estudante da Trybe.

# Entregáveis

<details>
  <summary><strong>🤷🏽‍♀️ Como entregar</strong></summary><br />

  Para entregar o seu projeto você deverá criar um *Pull Request* neste repositório.

  Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://app.betrybe.com/course/4d67f5b4-34a6-489f-a205-b6c7dc50fc16/) e nosso [Blog - Git & GitHub](https://blog.betrybe.com/tecnologia/git-e-github/) sempre que precisar!
</details>

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />
  <p align="center">
    <img src="/.images/job.png" alt="Logo Aplicação" width="300"/>
  </p>
  
  Neste projeto você implementará análises a partir de um conjunto de dados sobre empregos.

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

  🚵 Habilidades a serem trabalhadas:
  <ul>
    <li>Utilizar o terminal interativo do Python.</li>
    <li>Utilizar estruturas condicionais e de repetição.</li>
    <li>Utilizar funções built-in do Python.</li>
    <li>Utilizar tratamento de exceções.</li>
    <li>Realizar a manipulação de arquivos.</li>
    <li>Escrever funções.</li>
    <li>Escrever testes com Pytest.</li>
    <li>Escrever seus próprios módulos e importá-los em outros códigos.</li>
  </ul>
</details>

<details>
  <summary><strong>🗓 Data de Entrega</strong></summary><br />
  
  * Este projeto é individual;
  * Serão `1` dias de projeto;
  * Data para entrega no prazo regular: `01/04/2024 23:59`.

</details>

# Orientações
<details>
  <summary><strong>⚠ Antes de começar a desenvolver</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-034-project-job-insights.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-034-project-job-insights`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `main`

  - Verifique que você está na branch `main`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `main`
    - Exemplo: `git checkout main`
  - Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
    - Exemplo: `git checkout -b joaozinho-job-insights`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'iniciando o projeto job-insights'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin joaozinho-job-insights`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-034-project-job-insights/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-034-project-job-insights/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong>⌨️ Durante o desenvolvimento</strong></summary><br />

  - Faça `commits` das alterações que você fizer no código regularmente

  - Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

  - Os comandos que você utilizará com mais frequência são:
    1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
    2. `git add` _(para adicionar arquivos ao stage do Git)_
    3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
    4. `git push -u origin nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
    5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

</details>

<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── data
  │   └──🔸jobs.csv
  ├── src
  │   ├── insights
  │   │   ├──🔹industries.py
  │   │   ├──🔹jobs.py
  │   │   └──🔹salaries.py
  │   ├── pre_built
  │   │   ├──🔸brazilian_jobs.py
  │   │   ├──🔸counter.py
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├──🔸test_industries.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_salaries.py
  ```

  Na estrutura deste _template_, você deve implementar as funções necessárias. Novos arquivos e funções podem ser criados conforme a necessidade da sua implementação, porém não remova arquivos já existentes.

</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

  ⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
  ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).


</details>


<details>
  <summary><strong>🤝 Depois de terminar o desenvolvimento (opcional)</strong></summary><br />

  Para sinalizar que o seu projeto está pronto para o _"Code Review"_, faça o seguinte:

  - Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

    - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

    - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

    - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-034`.

  Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

</details>

<details>
  <summary><strong>🕵🏿 Revisando um pull request</strong></summary><br />

  Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.

</details>

<details>
  <summary><strong>🗣 Nos dê feedbacks sobre o projeto!</strong></summary><br />

Ao finalizar e submeter o projeto, não se esqueça de avaliar sua experiência preenchendo o formulário. 
**Leva menos de 3 minutos!**

[FORMULÁRIO DE AVALIAÇÃO DE PROJETO](https://be-trybe.typeform.com/to/ZTeR4IbH#cohort_hidden=CH34&template=betrybe/sd-0x-project-job-insights)

</details>

<details>
  <summary><strong>🗂 Compartilhe seu portfólio!</strong></summary><br />

  Agora que você finalizou os requisitos, chegou a hora de mostrar ao mundo que você aprendeu algo novo! 🚀

  Siga esse [**guia que preparamos com carinho**](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/a3cac6d2-5060-445d-81f4-ea33451d8ea4/section/d4f5e97a-ca66-4e28-945d-9dd5c4282085/day/eff12025-1627-42c6-953d-238e9222c8ff/lesson/49cb103b-9e08-4ad5-af17-d423a624285a) para disponibilizar o projeto finalizado no seu GitHub pessoal.

  Esse passo é super importante para ganhar mais visibilidade no mercado de trabalho, mas também é útil para manter um back-up do seu trabalho.

  E você sabia que o LinkedIn é a principal rede social profissional e compartilhar o seu aprendizado lá é muito importante para quem deseja construir uma carreira de sucesso? Compartilhe esse projeto no seu LinkedIn, marque o perfil da Trybe (@trybe) e mostre para a sua rede toda a sua evolução.

</details>

# Requisitos Obrigatórios

## 1 - Count Ocurrences (Testes)
> **Implemente em:** `tests/counter/test_counter.py`

  <p align="center">
    <img src="/.images/flask.png" alt="Imagem sobre contar ocorrências" width="600"/>
  </p>

A empresa cliente contratou um relatório que informa a quantidade de ocorrências das palavra *Python* e *Javascript* nos dados e, para isso, temos uma implementação pronta em `src/pre_built/counter.py`. Durante o desenvolvimento, sofremos com alguns `bugs`, que já foram resolvidos. Para termos certeza e confiança da nossa entrega, no entanto, e não corrermos riscos, precisaremos de *testes automatizados* que garantam isso!

O nome deste teste **deve** ser `test_counter`, e ele deve garantir que atenda estas especificações:

- **Chamar** a função `count_ocurrences` passando dois parâmetros:
  - `path` uma string com o caminho do arquivo (`data/jobs.csv`);
  - `word` uma string com a palavra a ser contabilizada;
- Garantir que a função retorna corretamente a quantidade de ocorrências da palavra solicitada;
  - A contagem de palavras deve ser _case insentitive_, ou seja, não diferenciar letras maiúsculas de minúsculas;


<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code> ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O teste rejeita implementações que não retornam a quantidade de palavras corretamente.
- O teste aprova implementações corretas.
- Se o teste não é um falso positivo, ou seja, teste que passa sem realmente testar o código.

</details>

## 2 - Implemente o método `read`
> **Implemente em:** `src/insights/jobs.py`

**Preparando para Processar Dados de Arquivos CSV com a Classe `ProcessJobs`**

O cliente ficou muito satisfeito com o excelente trabalho que você realizou, implementando todos os testes solicitados. Agora, eles estão empolgados para dar continuidade a um de seus projetos. A próxima etapa envolverá o processamento de dados contidos em arquivos CSV.

A classe ProcessJobs é fundamental nesse contexto, pois é responsável por lidar com operações relacionadas à leitura e processamento de dados sobre trabalhos a partir de um arquivo CSV. A classe apresenta métodos que permitem ler os dados de um arquivo CSV, obter tipos únicos de trabalhos e filtrar os trabalhos com base em seus tipos.

Antes de iniciar vamos compreender a funcionalidade da classe ProcessJobs. O código encontra-se no arquivo `src/insights/jobs.py`. Neste arquivo, você encontrará a implementação da classe ProcessJobs, que contém métodos específicos para realizar tarefas detalhadas, de acordo com os requisitos a seguir:

-----

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. E o método `read` será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários. 

- O método deve receber um _path_ (uma string com o caminho para um arquivo).
- O método deve abrir o arquivo e ler seus conteúdos.
- O método deve tratar o arquivo como CSV.
- O método read deve ler o csv e armazenar os dados em `self.jobs_list`, que será lista dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha. 


<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  Se o conteúdo do arquivo for:
  
```
nome,cidade,telefone
Ana,Curitiba,1111111
Bernardo,Santos,999999
```

  O retorno deverá ser: 
  
```python
  [
    {"nome": "Ana", "cidade": "Curitiba", "telefone": "1111111"},
    {"nome": "Bernardo", "cidade": "Santos", "telefone": "999999"}
  ]
```
</details> 

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

  Abra um terminal Python através do comando <code>python3 -i src/insights/jobs.py</code> crie uma instância da classe `ProcessJobs` e chame o método utilizando `read` diferentes _paths_.
  
  Exemplo: 

```py
instancia = ProcessJobs()
instancia.read('/caminho/do/arquivo')
```

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- O método abre o arquivo passado como parâmetro.
- O método retorna uma lista de dicionários.
- O método retorna a quantidade correta de itens na lista.
- Nos dicionários retornados, as chaves correspondem aos cabeçalhos do arquivo.

</details>

## 3 - Implemente o método `get_unique_job_types`
> **Implemente em:** `src/insights/jobs.py`

Agora já temos como carregar os dados e podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

- A função deve retornar uma lista de valores únicos presentes na coluna `job_type`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método utiliza os dados previamente carregados do arquivo, que estão armazenados em `self.jobs_list`, para identificar e retornar os tipos únicos de empregos presentes nessa lista.
- O método retorna a quantidade correta de valores.
- O método retorna os valores corretos.
- O método desconsidera valores vazios.

</details>

## 4 - Implemente o método `filter_by_multiple_criteria`
<p align="center">
  <img src="/.images/filter.png" alt="Contagem" width="400"/>
</p>

> **Implemente em:** `src/insights/jobs.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar mais um método na nossa classe `ProcessJobs`.

- O método deve receber uma lista de empregos representados por dicionários.
- Deve receber um dicionário filter_criteria que contém pares chave-valor, onde a - chave é o critério de filtragem (`industry` ou `job_type`) e o valor é o valor associado a esse critério.
- O método deve retornar uma lista de empregos que correspondem a todos os critérios fornecidos.

Exemplo do tipo de dado que o primeiro parâmetro do nosso método pode receber:

```python

jobs = [
    {"id": 1, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 2, "industry": "Healthcare", "job_type": "PART_TIME"},
    {"id": 3, "industry": "Finance", "job_type": "FULL_TIME"},
    {"id": 4, "industry": "IT", "job_type": "CONTRACTOR"},
    {"id": 5, "industry": "Healthcare", "job_type": "FULL_TIME"},
    {"id": 6, "industry": "Finance", "job_type": "PART_TIME"},
    {"id": 7, "industry": "IT", "job_type": "FULL_TIME"},
    {"id": 8, "industry": "Healthcare", "job_type": "CONTRACTOR"},
]
```
Exemplo de uso dos métodos:
```python

process_jobs = ProcessJobs()

# Filtrar por indústria "Healthcare" e tipo de emprego "PART_TIME"
result_by_multiple_criteria = process_jobs.filter_by_multiple_criteria(
    jobs, {"industry": "Healthcare", "job_type": "PART_TIME"}
)
```
<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método retorna a quantidade correta de valores.
- O método retorna os valores corretos.
- O método retorna os valores na ordem correta.
- O método retorna uma lista vazia para critérios ausentes nos empregos recebidos.
- O método deve lançar uma exceção `TypeError` quando o filtro fornecido para o método `filter_by_multiple_criteria` não é um dicionário. Exemplo:
```py
process_jobs.filter_by_multiple_criteria(jobs, "industry_and_job_type")
```
</details>

## 5 - Implemente o método `get_unique_industries`
> **Implemente em:** `src/insights/industries.py`

Agora iremos identificar quais indústrias estão representadas nesse conjunto de dados. Para facilitar o trabalho, a outra pessoa desenvolvedora envolvida no projeto já deixou a classe `ProcessIndustries` implementada herdando a classe `ProcessJobs`. 

- O método deve retornar uma lista de valores únicos presentes na coluna `industry`.
- O método desconsidera valores vazios.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método utiliza os dados previamente carregados do arquivo, que estão armazenados em `self.jobs_list`, para identificar e retornar os tipos únicos de empregos presentes nessa lista.
- O método retorna a quantidade correta de valores.
- O método retorna os valores corretos.

</details>

## 6 - Implemente o método `get_max_salary`
> **Implemente em:** `src/insights/salaries.py`

Dentro do arquivo mencionado, você encontrará a classe `ProcessSalaries`.

O método  `get_max_salary` deve extrair o maior salário dos dados que foram lidos e armazenados previamente na lista `self.jobs_list`. A classe `ProcessSalaries` herda funcionalidades da classe `ProcessJobs`, o que inclui a capacidade de acessar dados previamente lidos sem a necessidade de uma nova leitura do arquivo. 

Os dados contêm informações sobre as faixas salariais de cada emprego apresentado. Agora, nossa tarefa é identificar o valor mais alto entre todas essas faixas.

- O método deve ignorar os valores ausentes.
- O método deve retornar *um valor inteiro* com o maior salário presente na coluna.`max_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método usa a lista `self.jobs_list` que já foi preenchida pelo método `read`.
- O método retorna o valor correto.

</details>

## 7 - Implemente o método `get_min_salary`
> **Implemente em:** `src/insights/salaries.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o menor valor de todas as faixas.

O método  `get_min_salary` deve extrair o menor salário dos dados que foram lidos e armazenados previamente na lista `self.jobs_list`.

- O método deve ignorar os valores ausentes.
- O método deve retornar *um valor inteiro* com o menor salário presente na coluna `min_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método usa a lista `self.jobs_list` que já foi preenchida pelo método `read`.
- O método retorna o valor correto.
</details>


## 8 - Implemente o método `matches_salary_range`
> **Implemente em:** `src/insights/salaries.py`

O aplicativo vai precisar filtrar os empregos por salário também. Implemente o método `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

- O método deve receber um dicionário `job` como primeiro parâmetro, com as chaves `min_salary` e `max_salary`, que podem ser números ou strings que representem números.
- O método  deve receber um número ou string que represente o número `salary` como segundo parâmetro.
- O método deve lançar um erro `ValueError` nos seguintes casos:
  - alguma das chaves `min_salary` ou `max_salary` estão *ausentes* no dicionário;
  - alguma das chaves `min_salary` ou `max_salary` tem valores não-numéricos;
  - o valor de `min_salary` é maior que o valor de `max_salary`;
  - o parâmetro `salary` tem valores não numéricos;
- O método  deve retornar `True` se o salário procurado estiver dentro da faixa salarial ou `False` se não estiver.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método  retorna o booleano correto.
- O método lança um `ValueError` se o valor de `min_salary` for maior que o valor de `max_salary`.
- O método lança um `ValueError` se as chaves `min_salary` ou `max_salary` tiverem valores não numéricos.
  - Observação: strings que representem números são valores **válidos** para `min_salary` ou `max_salary`.
- O método lança um `ValueError` se o parâmetro `salary` tiver valor não numérico.
- O método lança um `ValueError` se as chaves `min_salary` ou `max_salary` estiverem ausentes no dicionário.
</details>

---

# Requisitos Bônus

## 9 (`Bônus`) - Implemente o método `filter_by_salary_range`
> **Implemente em:** `src/insights/salaries.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a método implementado no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

- O método deve receber uma lista de dicionários `jobs` como primeiro parâmetro.
- O método deve receber um número ou string `salary` como segundo parâmetro.
- O método deve ignorar os empregos com valores inválidos para `min_salary` ou `max_salary`.
  - Observação: strings que representem números são valores **válidos** para `min_salary` ou `max_salary`.
- O método deve retornar uma lista com todos os empregos onde o salário `salary`. estiver entre os valores da coluna `min_salary` e `max_salary`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O método retorna a quantidade correta de valores.
- O método retorna os valores corretos.
- O método retorna os valores na ordem correta.
- Empregos onde as chaves `min_salary` ou `max_salary` tiverem valores não numéricos devem ser ignorados.
- Empregos onde o valor de `min_salary` for maior que o valor de `max_salary` devem ser ignorados.
- Se `salary` for uma string que represente um número, o método deverá se comportar tal como se `salary` fosse um número.
- Se `salary` for uma string que não represente um número válido, deverá ser levantado um `ValueError`.
</details>


## 10 (`Bônus`) - Read Brazilian File (Testes)
> **Implemente em:** `tests/brazilian/test_brazilian_jobs.py`

*ps: O funcionamento da função criada para esse teste depende da implementação do método `read` em `jobs.py`*

A empresa cliente analisa relatórios em inglês, porém agora ela quer expandir seus negócios aqui para o Brasil e deseja analisar relatórios em português também. No entanto, as chaves do `dict` que usamos pra organizar os dados **devem** continuar em inglês. Ou seja: para gerar o relatório, deveremos ler as chaves em português e traduzi-las para inglês para povoar os nossos dados.

Nossa equipe já implementou essa função, a `read_brazilian_file`, na qual adotamos a estratégia de chamar o método original `read`, que implementamos no `requisito 1`, e depois traduzimos as chaves para o inglês. Agora precisamos criar testes para ter certeza que esta tudo certo!

O nome deste teste **deve** ser `test_brazilian_jobs`, e ele deve garantir que atenda as seguintes especificações:

- **Chamar** a função `read_brazilian_file` e ela deve receber um parâmetro:
  - `path` que é uma string com o caminho do arquivo csv em português (`tests/mocks/brazilians_jobs.csv`);
  - Retorna uma lista de dicionários com as chaves em inglês

<details>
  <summary>
    <b>📝Exemplo</b>
  </summary>
  O dicionário: <code>{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}</code>

  Deve ser traduzido para: <code>{"title": "Maquinista", "salary": "2000", "type": "trainee"}</code>
</details>  
<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code> ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- O teste rejeita implementações que não retornam as chaves traduzidas corretamente.
- O teste aprova implementações corretas.
- Se o teste não é um falso positivo, ou seja, teste que passa sem realmente testar o código.
</details>
