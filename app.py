from flask import Flask, request, render_template, redirect, url_for

# para iniciar nossa aplicação, iremos chamar o framework flask
app = Flask(__name__)

lista_produtos = [
    {"id":1, "nome":"Pão","tipo":"Padaria","preco":13.99},
    {"id":2, "nome":"Leite","tipo":"Alimento","preco":6.00},
    {"id":3, "nome":"Presunto","tipo":"Frio","preco":60.00}
] 

id_produto = 3

@app.route("/")
def pagina():
    return render_template("index.html",produtos=lista_produtos)

@app.post("/adicionar")
def adicionar():

    global id_produto

    n = request.form['nome']
    t = request.form['tipo']
    p = request.form['preco']
    id_produto = id_produto + 1

    novo_produto = {"id":id_produto,"nome":n,"tipo":t,"preco":p}

    # adicionar o novo produto a lista de produtos
    lista_produtos.append(novo_produto)

    # Após adicionar o produto a lista iremos redirecionar 
    # a página para a index.html, que irá exibir o novo produto
    # na tabela de produtos
    return redirect(url_for("pagina"))


@app.get("/editar/<int:id>")
def editar(id):

    prod = None
    for p in lista_produtos:
        if p['id']==id:
            prod = p
            break
            
    return render_template("editar.html",produto = prod)


@app.post("/atualizar/<int:id>")
def atualizar(id):
    i = id
    n = request.form['nome']
    t = request.form['tipo']
    p = float(request.form['preco'])

    prod = None
    for pr in lista_produtos:
        if( pr['id']==id):
            prod = pr
            break

    prod["nome"] = n
    prod["tipo"] = t
    prod["preco"] = p

    return redirect(url_for("pagina"))


@app.get("/apagar/<int:id>")
def apagar(id):
    
    global lista_produtos
    lista_produtos = [p for p in lista_produtos if p['id'] != id]


    return redirect(url_for("pagina"))


app.run(debug=True)