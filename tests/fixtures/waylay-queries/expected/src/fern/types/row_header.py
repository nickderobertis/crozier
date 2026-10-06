

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp import Timestamp
from .timestamp_iso import TimestampIso


class RowHeader(UniversalBaseModel):
    """
    Index entry attributes.

    Attributes for a timestamp index entry.
    """

    timestamp: Timestamp
    timestamp_iso: typing.Optional[TimestampIso] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
