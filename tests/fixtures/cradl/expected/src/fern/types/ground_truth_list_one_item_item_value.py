

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .ground_truth_list import GroundTruthList
GroundTruthListOneItemItemValue = typing.Union[
    typing.Optional[str], typing.Optional[bool], typing.Optional[float], "GroundTruthList"
]
