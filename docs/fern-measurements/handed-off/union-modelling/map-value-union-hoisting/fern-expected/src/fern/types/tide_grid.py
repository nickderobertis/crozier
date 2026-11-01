

import typing

from .tide_grid_item_item_value import TideGridItemItemValue

TideGrid = typing.List[typing.List[typing.Dict[str, TideGridItemItemValue]]]
"""
Rows of columns of readings keyed by gauge.
"""
