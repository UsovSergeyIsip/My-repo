[main.py](https://github.com/user-attachments/files/28311162/main.py)
from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles
import uvicorn

Приложение = FastAPI()

class КлассРепозитоия:
    def __init__(self): # self атрибут ссылка на обьект
        self.toys = []
        self.next_id = 1
    def получить_все(self):
        return self.toys

    def получить_по_айди(self, toy_id):
        for t in self.toys: 
            if t["id"] == toy_id:
                return t
        return None

    def добавление(self, locomotive_number: int, car_count: int, material: str, description: str):
        toy = {
            "id": self.next_id,
            "locomotive_number": locomotive_number,
            "car_count": car_count,
            "material": material,
            "description": description
        }
        self.toys.append(toy)
        self.next_id += 1
        return toy

    def обновление(self, toy_id: int, locomotive_number=None, car_count=None, material=None, description=None):
        toy = self.получить_по_айди(toy_id)
        if not toy:
            return None
        if locomotive_number is not None:
            toy["locomotive_number"] = locomotive_number
        if car_count is not None:
            toy["car_count"] = car_count
        if material is not None:
            toy["material"] = material
        if description is not None:
            toy["description"] = description
        return toy

    def удаление(self, toy_id: int):
        self.toys = [t for t in self.toys if t["id"] != toy_id]

ЭкземплярРепозитория = КлассРепозитоия()
@Приложение.get("/api")
def получение_всех():
    return ЭкземплярРепозитория.получить_все()

@Приложение.post("/api/create")
def создание(req: dict):
    return ЭкземплярРепозитория.добавление(
        int(req["locomotive_number"]),
        int(req["car_count"]),
        str(req["material"]),
        str(req["description"])
    )

@Приложение.get("/api/get/{toy_id}")
def получение_по_айди(toy_id: int):
    toy = ЭкземплярРепозитория.получить_по_айди(toy_id)
    if toy is None:
        return {"error": "Not found"}
    return toy

@Приложение.post("/api/update/{toy_id}") 
def обновление(toy_id: int, req: dict):
    return ЭкземплярРепозитория.обновление(
        toy_id,
        locomotive_number=int(req.get("locomotive_number")) if req.get("locomotive_number") is not None else None,
        car_count=int(req.get("car_count")) if req.get("car_count") is not None else None,
        material=str(req.get("material")) if req.get("material") is not None else None,
        description=str(req.get("description")) if req.get("description") is not None else None
    )

@Приложение.post("/api/delete/{toy_id}")
def удаление(toy_id: int):
    ЭкземплярРепозитория.удаление(toy_id)
    return {"ok": True}

Приложение.mount("/", StaticFiles(directory="static", html=True), name="static")
uvicorn.run(Приложение, host="127.0.0.1", port=8000)


