from fastapi import FastAPI, HTTPException

app = FastAPI()

# Implementacion de la función process_orders según las especificaciones
def process_orders(orders, criterion):
    if criterion == "completed":
        filtered_orders = [order for order in orders if order["status"] == "completed"]
    elif criterion == "pending":
        filtered_orders = [order for order in orders if order["status"] == "pending"]
    elif criterion == "canceled":
        filtered_orders = [order for order in orders if order["status"] == "canceled"]
    elif criterion == "all":
        filtered_orders = orders
    else:
        raise HTTPException(status_code=400, detail="Criterio no válido")

    total_revenue = sum(order["price"] * order["quantity"] for order in filtered_orders)
    return total_revenue

# Implementacion del endpoint /solution
@app.post("/solution")
async def calculate_total_revenue(data: dict):
    orders = data.get("orders", [])
    criterion = data.get("criterion", "all")

    if any(order["price"] < 0 for order in orders):
        raise HTTPException(status_code=400, detail="El precio de un artículo no puede ser negativo")

    total_revenue = process_orders(orders, criterion)
    return {"total_revenue": total_revenue}
