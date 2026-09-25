

import typing

from .ground_truth_list import GroundTruthList

PatchDocumentIdGroundTruthItemValue = typing.Union[
    typing.Optional[str], typing.Optional[bool], typing.Optional[float], GroundTruthList
]
