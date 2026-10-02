from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title = "Gotham Inventory Service",
    description=(
        "Internal API for managing orders in Gotham Inventory.\n"
        "Handle creation, tracking of orders."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi/json"
)

@app.get("/")
def read_root():
    """Root endpoint - Health check"""
    return {
        "message" : "Welcome to gotham inventory",
        "status": "Healthy"
    }
    # FastAPI converts dict in JSON automatically

@app.get("/about")
def about():
    """Returns API metadata"""
    return {
        "service": "order-service",
        "team": "backend platform",
        "region": "ap-south-1",
        "version": "1.0.0"
    }


@app.get("/orders")
def orders():
    """List of orders from the inventory"""
    return {
        "orders": [
            {
                "id": 1,
                "name": "batmobile",
                "status": "delivered"
            },
            {
                "id": 2,
                "name": "batsuit",
                "status": "not delivered"
            },
            {
                "id": 3,
                "name": "catwomen's bike",
                "status": "delivered"
            }
        ]
    }


@app.get("/order/status")
def order_status():
    """Get order status"""
    return {
        "total_today": 2_50_263,
        "most_ordered": "metropolis"
    }


@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspect the raw request"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params)
    }


@app.get(
    "orders/active",
    summary="Get active orders",
    description=(
        "Returns all orders that are currrently being prepared, "
        "or delivery"
    ),
    tags=["Orders"],
    response_description="List of active orders objects",
    deprecated=False
)
def get_active_orders():
    """All the active orders"""
    return {
        "active_orders": [
            {
                "id": 2,
                "name": "batsuit",
                "status": "not delivered"
            },
            {
                "id": 4,
                "name": "cryptonite",
                "status": "out for delivery"
            }
        ]
    }