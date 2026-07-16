

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_response import BadResponse


class BadResponsesFaultConfig(UniversalBaseModel):
    """
    Config for bad requests injection fault
    """

    ratio: float = pydantic.Field()
    """
    The percentage of requests affected by this fault. Value should be between 0.0 and 1.0
    """

    responses: typing.List[BadResponse] = pydantic.Field()
    """
    The possibles responses
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
