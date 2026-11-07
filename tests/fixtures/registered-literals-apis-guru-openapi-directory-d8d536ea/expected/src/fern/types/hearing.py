

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_structured_data import SourceStructuredData


class Hearing(UniversalBaseModel):
    first_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="firstFetchDate"),
        pydantic.Field(alias="firstFetchDate", description="When this hearing was first fetched from the source."),
    ]
    """
    When this hearing was first fetched from the source.
    """

    hearing_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="hearingDate"), pydantic.Field(alias="hearingDate", description="Hearing Date")
    ]
    """
    Hearing Date
    """

    hearing_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hearingDescription"),
        pydantic.Field(alias="hearingDescription", description="Source Hearing Description Text"),
    ] = None
    """
    Source Hearing Description Text
    """

    hearing_structured: typing_extensions.Annotated[
        typing.Optional[SourceStructuredData],
        FieldMetadata(alias="hearingStructured"),
        pydantic.Field(alias="hearingStructured"),
    ] = None
    last_fetch_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(alias="lastFetchDate", description="When this hearing was last fetched from the source."),
    ]
    """
    When this hearing was last fetched from the source.
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    Location where the hearing will takeplace.
    """

    object: str = pydantic.Field()
    """
    Name of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
