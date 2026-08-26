

import typing

from .create_cell import CreateCell
from .delete_cell import DeleteCell
from .move_cell import MoveCell
from .reorder_cells import ReorderCells
from .set_code import SetCode
from .set_config import SetConfig
from .set_name import SetName

NotebookDocumentTransactionRequestChangesItem = typing.Union[
    CreateCell, DeleteCell, MoveCell, ReorderCells, SetCode, SetName, SetConfig
]
