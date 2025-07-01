# Agenda de Cuidados para Pets
Aplicação web desenvolvida em Pyython e Django para ajudar tutores de pets a organizarem os cuidados com seus animais de forma visual e prática.

## Desenvolvido para
Disciplina **CC6PDSW – Projeto e Desenvolvimento de Sistemas Web**  por Fernanda F. Matioli e Diego L. H. Dallaqua
Curso de Ciência da Computação – UTFPR – Campus Santa Helena  
Semestre 2025/1

## Como rodar o projeto localmente

### 1. Clone o repositório (pule esse tópico se já tiver o código em zip)
git clone https://github.com/seu-usuario/agenda-cuidados-pets.git
cd agenda-cuidados-pets

### 2. Crie e ative o ambiente virtual

**Windows:**
python -m venv venv
venv\Scripts\activate

**Linux/macOS:**
python3 -m venv venv
source venv/bin/activate

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Realize as migrações

python manage.py makemigrations
python manage.py migrate

### 5. Inicie o servidor de desenvolvimento

python manage.py runserver

Abra o navegador e acesse:  
[http://127.0.0.1:8000]