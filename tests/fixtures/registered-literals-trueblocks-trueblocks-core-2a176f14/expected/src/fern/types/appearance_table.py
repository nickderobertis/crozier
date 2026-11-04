

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_record import AppRecord


class AppearanceTable(UniversalBaseModel):
    """
    an appearance table for an address
    """

    address_record: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="AddressRecord"),
        pydantic.Field(alias="AddressRecord", description="the address record for these appearances"),
    ] = None
    """
    the address record for these appearances
    """

    appearances: typing_extensions.Annotated[
        typing.Optional[typing.List[AppRecord]],
        FieldMetadata(alias="Appearances"),
        pydantic.Field(alias="Appearances", description="all the appearances for this address"),
    ] = None
    """
    all the appearances for this address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
