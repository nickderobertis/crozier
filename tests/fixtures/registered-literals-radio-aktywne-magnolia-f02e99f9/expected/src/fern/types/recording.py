

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .naive_datetime import NaiveDatetime


class Recording(UniversalBaseModel):
    """
    Recording data.
    """

    event: str = pydantic.Field()
    """
    Identifier of the event.
    """

    start: NaiveDatetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
