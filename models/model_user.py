from pydantic import BaseModel
from typing import Optional, List


class Asistencia(BaseModel):
    id: Optional[str] = None
    start: str
    end: str
    title: str


class Materia(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = "Lengua"
    nota_1: float
    nota_2: float
    promedio: float


class Alumno(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    userName: str
    password: str
    asistencias: List[Asistencia]
    materias: List[Materia]


class Padre(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    userName: str
    password: str
    hijos: List[Alumno]


class Docente(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    userName: str
    password: str
    materia: str
    materia: List[Alumno]


class Admin(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    userName: str
    password: str
