"""Greet a person by name."""


def greet(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned}"


if __name__ == "__main__":
    print(greet("world"))
