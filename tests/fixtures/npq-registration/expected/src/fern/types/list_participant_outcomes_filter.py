

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListParticipantOutcomesFilter(UniversalBaseModel):
    """
    Filter NPQ outcomes to return more specific results
    """

    created_since: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only records that have been created since this date and time (ISO 8601 date format)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
