from flask import Flask, render_template, request

app = Flask(__name__)

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    # Botões de habilidades
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    # Formulário de feedback
    email = request.form.get('email', '')
    texto = request.form.get('text', '')

    # Lógica para salvar as informações em um arquivo de texto
    # Verificamos se email e texto não estão vazios antes de salvar
    if email and texto:
        with open('feedback.txt', 'a', encoding='utf-8') as f:
            f.write(f"Email: {email} | Comentário: {texto}\n")

    return render_template('index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db,
        email=email,
        texto=texto
    )

if __name__ == "__main__":
    app.run(debug=True)
