# NexStage

<p align="center">
  <strong>Vagas de estágio em Guanambi - BA</strong><br>
  Uma plataforma para aproximar estudantes, empresas e oportunidades.
</p>

<p align="center">
  <a href="#objetivo">Objetivo</a> ·
  <a href="#como-funciona">Como funciona</a> ·
  <a href="#recursos">Recursos</a> ·
  <a href="#como-executar">Como executar</a>
</p>

<p align="center">
  <img src="static/assets/img/bg-img/6.jpg" alt="Imagem de capa do NexStage: vista panorâmica de uma cidade" width="100%">
</p>

> **NexStage** é um Sistema de Gerenciamento de Vagas para Estágio. O projeto centraliza oportunidades e organiza o acompanhamento das candidaturas em um só lugar.

<details>
<summary><strong>Sumário</strong></summary>

- [Objetivo](#objetivo)
- [Como funciona](#como-funciona)
- [Recursos](#recursos)
- [Tecnologias](#tecnologias)
- [Como executar](#como-executar)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Próximos passos](#próximos-passos)

</details>

## Objetivo

O NexStage foi desenvolvido como Projeto de Conclusão de Curso para facilitar a divulgação e a busca por estágios, com foco em Guanambi - BA. A plataforma oferece aos candidatos um lugar para encontrar oportunidades e acompanhar suas candidaturas, enquanto permite às empresas publicar vagas e organizar os interessados.

## Como funciona

O diagrama resume o fluxo principal para cada perfil:

~~~mermaid
flowchart LR
    Candidato["Candidato"] --> Buscar["Busca vagas ativas"]
    Buscar --> Inscrever["Envia candidatura e currículo"]
    Inscrever --> Acompanhar["Acompanha status no painel"]

    Empresa["Empresa"] --> Publicar["Publica e gerencia vagas"]
    Publicar --> Receber["Consulta candidatos inscritos"]
    Receber --> Decidir{"Atualiza candidatura"}
    Decidir -->|Aceitar| Aprovada["Aprovada"]
    Decidir -->|Manter| Analise["Em análise"]
    Decidir -->|Recusar| Rejeitada["Rejeitada"]
    Aprovada --> Acompanhar
    Analise --> Acompanhar
    Rejeitada --> Acompanhar
~~~

### Candidato

1. Cria uma conta e completa o perfil, incluindo o currículo.
2. Pesquisa vagas por título, empresa ou área.
3. Envia uma candidatura para uma vaga ativa.
4. Consulta os detalhes e acompanha o status pelo painel.

### Empresa

1. Cria uma conta de empresa e acessa seu painel.
2. Publica, edita e acompanha suas vagas.
3. Consulta os currículos e os dados de quem se candidatou.
4. Aceita, mantém em análise ou recusa cada candidatura. O status atualizado fica visível para o candidato no painel.
5. Desativa vagas encerradas. A desativação remove a vaga das buscas e preserva o histórico e as candidaturas.

## Recursos

| Área | O que oferece |
| --- | --- |
| Vagas | Listagem, pesquisa, detalhes e filtro automático de vagas desativadas |
| Candidaturas | Envio de currículo e mensagem, detalhes e status |
| Painel do candidato | Perfil, lista de candidaturas e atualizações de status |
| Painel da empresa | Publicação e edição de vagas, inscritos e gestão de status |
| Acesso | Login e cadastro separados para candidatos e empresas |
| Histórico | Desativação lógica de vagas para preservar candidaturas existentes |

<details>
<summary><strong>Status de uma candidatura</strong></summary>

- **Em análise**: candidatura recebida ou ainda em avaliação.
- **Aprovada**: empresa aceitou a candidatura.
- **Rejeitada**: empresa recusou a candidatura.

O candidato vê o status atualizado no painel e na página de detalhes da candidatura.

</details>

## Tecnologias

- **Python**
- **Django 5.2** — aplicação web e acesso administrativo
- **SQLite** — banco de dados local padrão
- **HTML e CSS** — páginas responsivas

## Como executar

Os comandos abaixo devem ser executados dentro da pasta do projeto (NexStage).

### 1. Criar e ativar um ambiente virtual

~~~powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
~~~

No macOS ou Linux, use:

~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

### 2. Instalar as dependências e preparar o banco

~~~bash
python -m pip install -r requirements.txt
python manage.py migrate
~~~

### 3. Iniciar o servidor

~~~bash
python manage.py runserver
~~~

Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador. Para criar uma conta administrativa local, execute <code>python manage.py createsuperuser</code>.

<details>
<summary><strong>Comandos úteis</strong></summary>

| Comando | Para que serve |
| --- | --- |
| <code>python manage.py migrate</code> | Aplica as migrations ao banco |
| <code>python manage.py createsuperuser</code> | Cria um usuário para a administração |
| <code>python manage.py runserver</code> | Inicia o servidor local |
| <code>python manage.py check</code> | Verifica a configuração do projeto |

</details>

## Estrutura do projeto

~~~text
NexStage/
├── meu_app/           # Modelos, formulários, views, URLs e migrations
├── meu_projeto/       # Configurações Django e URLs principais
├── template/          # Templates HTML
├── static/            # CSS, JavaScript e imagens
├── media/             # Currículos enviados durante o uso local
├── manage.py
└── requirements.txt
~~~

## Próximos passos

O NexStage pode evoluir com notificações por e-mail, filtros adicionais para vagas, paginação e implantação em um servidor com banco de dados de produção.

---

<p align="center"><sub>Projeto de Conclusão de Curso · Técnico em Informática para Internet · IF Baiano — Campus Guanambi</sub></p>
