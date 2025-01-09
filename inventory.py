import json
import uuid

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_product(name, category, quantity, price):
    data = load_data()
    new_product = {
        "id": str(uuid.uuid4()),
        "name": name,
        "category": category,
        "quantity": int(quantity),
        "price": float(price)
    }
    data.append(new_product)
    save_data(data)
    print("Produto adicionado com sucesso!")

def list_products():
    data = load_data()
    if data:
        from tabulate import tabulate
        print(tabulate(data, headers="keys", tablefmt="pretty"))
    else:
        print("Nenhum produto cadastrado.")

def update_product(product_id, updates):
    data = load_data()
    for product in data:
        if product["id"] == product_id:
            product.update(updates)
            save_data(data)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

def delete_product(product_id):
    data = load_data()
    for product in data:
        if product["id"] == product_id:
            data.remove(product)
            save_data(data)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

def search_product(term):
    data = load_data()
    results = [product for product in data if term.lower() in product["name"].lower() or term == product["id"]]
    if results:
        from tabulate import tabulate
        print(tabulate(results, headers="keys", tablefmt="pretty"))
    else:
        print("Nenhum produto encontrado.")
