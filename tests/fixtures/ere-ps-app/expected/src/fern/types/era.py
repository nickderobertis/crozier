

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class Era(UniversalBaseModel):
    name: typing.Optional[str] = None
    abbr: typing.Optional[str] = None
    since: typing.Optional[int] = None
    since_date: typing_extensions.Annotated[
        typing.Optional["CalendarDate"], FieldMetadata(alias="sinceDate"), pydantic.Field(alias="sinceDate")
    ] = None
    local_time: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="localTime"), pydantic.Field(alias="localTime")
    ] = None
    hash: typing.Optional[int] = None
    abbreviation: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .calendar_date import CalendarDate

update_forward_refs(Era, CalendarDate=CalendarDate)
