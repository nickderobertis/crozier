

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature_discouraged_according_to import FeatureDiscouragedAccordingTo
from .feature_discouraged_alternative import FeatureDiscouragedAlternative


class FeatureDiscouragedInfo(UniversalBaseModel):
    according_to: typing.Optional[typing.List[FeatureDiscouragedAccordingTo]] = None
    alternatives: typing.Optional[typing.List[FeatureDiscouragedAlternative]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
