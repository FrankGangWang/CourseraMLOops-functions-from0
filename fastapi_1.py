from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None


app = FastAPI()  # FastAPI instance


@app.get("/")
async def hello():
    return {"Hello": "World"}


@app.post("/package")
async def make_package(package: Package):  # endpoint
    print(f"package type={type(package)}")
    print(f"package={package}")
    package.name = package.name + ":" + package.number
    print(f"package={package}")
    return f"Post response at endpoint /package: {package}"
