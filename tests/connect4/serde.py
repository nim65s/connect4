from .game import Cell, Grid


def serialize_cell(cell: Cell) -> str:
    ...


def deserialize_cell(cell: str) -> Cell:
    ...


def serialize_grid(grid: Grid) -> str:
    ...


def deserialize_grid(grid: str) -> Grid:
    ...
