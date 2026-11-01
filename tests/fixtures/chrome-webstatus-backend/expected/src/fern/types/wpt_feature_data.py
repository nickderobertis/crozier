

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WptFeatureData(UniversalBaseModel):
    score: typing.Optional[float] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Contains optional metadata about the metric. This key-value pair is to be considered unstable and can change at any moment. If a field here becomes mature, we can add it to the main WPTFeatureData definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
