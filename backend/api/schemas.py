from pydantic import BaseModel


# --------------------------------------------------
# Request Models
# --------------------------------------------------

class ChurnRequest(BaseModel):
    recency: int
    frequency: int
    monetary: float


# --------------------------------------------------
# Response Models
# --------------------------------------------------

class HealthResponse(BaseModel):
    status: str


class HomeResponse(BaseModel):
    application: str
    version: str


class ChurnResponse(BaseModel):
    prediction: str


class DashboardResponse(BaseModel):
    revenue: float
    orders: int
    customers: int
    average_order_value: float