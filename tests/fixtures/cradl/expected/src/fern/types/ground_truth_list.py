

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .ground_truth_list_one_item_item import GroundTruthListOneItemItem
    from .ground_truth_list_zero_item import GroundTruthListZeroItem
GroundTruthList = typing.Union[
    typing.List["GroundTruthListZeroItem"], typing.List[typing.List["GroundTruthListOneItemItem"]]
]
