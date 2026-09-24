

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Location(UniversalBaseModel):
    location: str = pydantic.Field()
    """
    The location (RFID tag)
    """

    scanned_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="scannedAt"),
        pydantic.Field(alias="scannedAt", description="The date and time when the location was scanned"),
    ]
    """
    The date and time when the location was scanned
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
