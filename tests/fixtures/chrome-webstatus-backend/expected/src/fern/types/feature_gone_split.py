

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .basic_error_model import BasicErrorModel
from .feature_gone_split_type import FeatureGoneSplitType
from .feature_split_info import FeatureSplitInfo


class FeatureGoneSplit(BasicErrorModel):
    type: FeatureGoneSplitType = pydantic.Field()
    """
    Indicates the feature was removed due to a split.
    """

    new_features: typing.List[FeatureSplitInfo] = pydantic.Field()
    """
    A list of feature IDs that have completely replaced the original, now-gone feature, as a result of a full split.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
