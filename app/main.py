from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title=" Task Manager API",
    description="Mini API para gestionar reservas",
    version="1.0.0"
)
class ReservationCreate(BaseModel):
    title: str
    description: str | None = None
    
class Reservation(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False
    
reservations: list[Reservation] = []
next_id = 1

@app.get("/")
def home():
    return {
        "message": "Bienvenido a Task Manager API",
        "docs": "/docs"
    }


@app.get("/reservations")
def list_reservations():
    return reservations

@app.post("/reservations")
def create_reservation(reservation_data: ReservationCreate):
    global next_id

    new_reservation = Reservation(
        id=next_id,
        title=reservation_data.title, # sería el asunto (Cumpleaños, Aniversario, etc.)
        description=reservation_data.description, #número de personas, fecha, hora, etc.
        completed=False
    )

    reservations.append(new_reservation)
    next_id += 1

    return {
        "message": "Reserva creada correctamente",
        "reservation": new_reservation
    }

@app.put("/reservations/{reservation_id}/complete")
def complete_reservation(reservation_id: int):
    for reservation in reservations:
        if reservation.id == reservation_id:
            reservation.completed = True
            return {
            "message": "Reserva completada",
            "reservation": reservation
            }
    raise HTTPException(status_code=404, detail="Reserva no encontrada")

