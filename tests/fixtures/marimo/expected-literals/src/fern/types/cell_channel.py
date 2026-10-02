

import typing

CellChannel = typing.Union[
    typing.Literal["marimo-error", "media", "output", "pdb", "stderr", "stdin", "stdout"], typing.Any
]
