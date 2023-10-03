from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title: str
    author_name: str

    def __repr__(self) -> str:
        return f"{self.title} by {self.author_name}"