# Customizando o comportamento do `django.contrib.auth`.

## O que queremos?

1. Não criar as permissões padrões automaticamente (add, delete, view, read).
2. Criar roles com conjuntos de permissões através de grupos.
3. Alterar o padrão de código de permissão que é add_model, delete_model, 
para app_label.model.add, app_label.view.access.
4. Poder adicionar permissões default para todas as classes do app.

## Como funciona?

A app `custom_permissions` faz o _patch_ de duas funções no `django.contrib.auth`.

Uma delas é responsável pelo formato e outra pela lista de permissões padrões.

## Como usar?

1. Copie a pasta `custom_permissions` para o seu projeto.
2. Instale a app `custom_permissions` no `INSTALLED_APPS` *antes* do `django.contrib.auth`.

## Como testar?

```
git clone git@github.com:henriquebastos/django-custom-permissions.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate -v 3
python -c 'import sqlite3; print(sqlite3.connect("db.sqlite3").cursor().execute("SELECT * from auth_permission").fetchall())'
```

O resultado deve ser:

`[(1, 7, 'core.blog.rename', 'Can rename title.'), (2, 7, 'core.blog.publish', 'Can publish post.')]`

_Nota:_ Observe que no migrate apenas as permissões explícitas do modelo `Blog` serão criadas.
