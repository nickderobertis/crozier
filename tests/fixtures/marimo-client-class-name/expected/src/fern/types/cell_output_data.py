

import typing

from .cell_output_data_one_item import CellOutputDataOneItem

CellOutputData = typing.Union[str, typing.List[CellOutputDataOneItem], typing.Dict[str, typing.Any]]
