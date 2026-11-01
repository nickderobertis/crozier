

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FeatureDeveloperSignals(UniversalBaseModel):
    upvotes: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of positive feedback for a feature
    """

    link: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the issue tracking developer signal for a feature.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
