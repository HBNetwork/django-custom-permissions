# django-custom-permissions


## Pontos do ACL

1. Não criar as permissões padrões automaticamente.
  1.1 Ou poder remover as permissões default de algumas classes.
2. Criar roles com conjuntos de permissões.
3. Alterar o padrão de código de permissão que é add_model, delete_model, 
para app_label.model.add, app_label.view.access.
4. Poder adicionar permissões default para todas as classes do app.
5. Ensaiar como seria o uso desse sistema de permissões sem contemplar modelos.

## Alternativas

Pesquisar outros apps de permissões.