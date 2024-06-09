from flask import Flask, render_template
from models import Recipe, Categoty

app = Flask(__name__)

sobremesa = Categoty(1,'Sobremesa')
salgados = Categoty(2, 'Salgados e Lanches')
bolos_doces = Categoty(3, 'Bolos e Doces')

bolo_cenoura = Recipe(1, 'Bolo de Cenoura', 'Bolo de cenoura fofinho com cobertura de cholocate ao leite, feito a partir de ingredientes frescos e saboroso', 40, 20, 'bolo-de-cenoura-recheado.jpg', [bolos_doces], 'Lucas Furtado', 'https://www.youtube.com/embed/L1czIgvo3-I?si=PjHLKpwcocIi_2OK')
bolo_chocolate = Recipe(2, 'Bolo de Chocolate', 'Bolo de chocolate vulcão fofinho com cobertura de cholocate ao leite, feito a partir de ingredientes frescos e saboroso', 35, 18, 'bolo-de-chocolate-recheado.jpg', [bolos_doces], 'Lucas Furtado', 'https://www.youtube.com/embed/QFMxJWh3mqE?si=_QkCQV7K6IV_Ignw')
pastel_carne = Recipe(3, 'Pastel de Carne', 'Massa de pastel recheada com carne moida fresca, temperada com cebola e alho, fritos em óleo quente.', 20, 8, 'pastel-carne.jpg', [salgados], 'Noel Rosa', 'https://www.youtube.com/embed/_vKR5jNYzVc?si=u0BDOgpl2UpUUtB9')
pudim_leite = Recipe(4, 'Pudim de Leite Condensado', 'Sobremesa deliciosa feita com leite condensado, ovo, leite, açucar. Cozido em banho maria com uma deliciosa calda de caramelo.', 90, 15, 'pudim-leite.jpg', [sobremesa], 'Tiago Carneiro', 'https://www.youtube.com/embed/0MJep0plDlw?si=6UsZFjaNc_sJ2aX8')

recipe_list=[bolo_cenoura, bolo_chocolate, pastel_carne, pudim_leite]
category_list=[sobremesa, salgados, bolos_doces]

@app.route('/')

def index():
    return render_template("pages/home.html", recipes = recipe_list, category = category_list)
    


@app.route('/receita/<int:id>')

def recipe(id:int):

    for recipes in recipe_list:
        if recipes.id == id:
            return render_template("pages/recipe.html", recipe = recipes)
    return "<h1>Ops! Receita não encontrada!</h1>"


@app.route('/categorias/<int:id>')

def category(id: int):
    categoria_encontrada = None
    for categories in category_list:
        if categories.id == id:
            categoria_encontrada = categories
            break 
    if not categoria_encontrada:
        return "<h1>Ops! Categoria não encontrada!</h1>"
    filtered_recipes = [recipe for recipe in recipe_list if any(cat.id == id for cat in recipe.category)]
    if not filtered_recipes:
        return "<h1>Ops! Nenhuma receita encontrada para esta categoria!</h1>"
    return render_template("pages/category.html", recipes=filtered_recipes, category = category_list)

            