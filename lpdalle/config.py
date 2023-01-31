import os
from dataclasses import dataclass


@dataclass
class Config:
    name: str
    user: str
    password: str
    host: str
    port: str


def load() -> Config:
    return Config(
        name=os.environ['NAME'],
        user=os.environ['USER'],
        password=os.environ['PASSWORD'],
        host=os.environ['HOST'],
        port=os.environ['PORT'],
    )


conf = load()
