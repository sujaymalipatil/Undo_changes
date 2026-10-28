"""Keep only the unique items, in first-seen order."""


def unique(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        result.append(item)
    return result


if __name__ == "__main__":
    print(unique([1, 2, 2, 3, 1]))
