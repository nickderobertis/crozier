

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address


class ConsensusNetworkHardforkFoundation(UniversalBaseModel):
    height: int
    primary_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="primaryAddress"), pydantic.Field(alias="primaryAddress")
    ]
    failsafe_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="failsafeAddress"), pydantic.Field(alias="failsafeAddress")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
