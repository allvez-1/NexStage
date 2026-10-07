# NextStage
NesxtStage - Sistema de Gerenciamento de Vagas para Estágio 

## Candidaturas e ciclo de vida das vagas

- O candidato acessa os detalhes de cada candidatura pelo painel em `/painel/candidato/candidaturas/<id>/`. A página apresenta o status, a data de envio, a vaga, a mensagem e o currículo associado. Cada candidatura só pode ser consultada pelo candidato proprietário.
- Os status disponíveis são **Em análise**, **Aprovada** e **Rejeitada**. Novas candidaturas começam como **Em análise**. A alteração do status pode ser feita pelo Django Admin.
- No painel da empresa, em “Candidatos”, é possível aceitar, manter em análise ou recusar cada candidatura. O status atualizado fica visível no painel e nos detalhes da candidatura do candidato.
- Uma empresa autenticada é direcionada ao próprio painel ao acessar a rota inicial; o menu e o rodapé oferecem acesso ao painel e às vagas, sem apresentar o fluxo de cadastro de outra empresa. Após sair da conta, a página inicial volta a ser o destino.
- A ação “Desativar” no painel da empresa marca a vaga como inativa. Vagas inativas deixam de aparecer nas buscas e não aceitam novas candidaturas, mas permanecem no painel da empresa e preservam as candidaturas existentes.
- Para aplicar o campo de status das candidaturas em um banco existente, execute `python manage.py migrate` dentro da pasta `NexStage`.
