

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .archive_record import ArchiveRecord


class Unit(UniversalBaseModel):
    aliases: typing.Optional[typing.List[str]] = None
    archive_record: typing_extensions.Annotated[
        typing.Optional[ArchiveRecord], FieldMetadata(alias="archiveRecord"), pydantic.Field(alias="archiveRecord")
    ] = None
    conversion_factor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="conversionFactor"),
        pydantic.Field(
            alias="conversionFactor", description="A decimal string relating this unit to its type's base unit"
        ),
    ] = None
    """
    A decimal string relating this unit to its type's base unit
    """

    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    symbol: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
