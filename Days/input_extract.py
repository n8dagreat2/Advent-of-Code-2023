def input_extract(file_name: str):
    """Given a file name, return a list of the extracted lines."""
    with open(
        file_name,
        "r",
    ) as f:
        return f.readlines()
