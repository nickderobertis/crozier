

import typing

from .ground_truth_list import GroundTruthList

PostDocumentsGroundTruthItemValue = typing.Union[
    typing.Optional[str], typing.Optional[bool], typing.Optional[float], GroundTruthList
]
