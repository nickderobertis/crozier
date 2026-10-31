

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature_split_info import FeatureSplitInfo


class FeatureEvolutionSplit(UniversalBaseModel):
    """
    Details if this feature's scope has been narrowed and parts of it have been spun off into new, distinct features.
    """

    features: typing.List[FeatureSplitInfo]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
