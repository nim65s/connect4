from .game import Cell, Grid


def serialize_cell(cell: Cell) -> str:
    """Render a cell as an ASCII character."""
    ...


def deserialize_cell(cell: str) -> Cell:
    """Take an ASCII character and return the corresponding Cell."""
    ...


def serialize_grid(grid: Grid) -> str:
    """Transform a Grid into a string of 42 concatenated Cell representations."""
    ...


def deserialize_grid(grid: str) -> Grid:
    """Transform a string containing 42 Cell representations and generate the
    corresponding Grid."""
    ...
