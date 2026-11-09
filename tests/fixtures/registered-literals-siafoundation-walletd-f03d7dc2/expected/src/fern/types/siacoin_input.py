

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .siacoin_output_id import SiacoinOutputId
from .unlock_conditions import UnlockConditions


class SiacoinInput(UniversalBaseModel):
    parent_id: typing_extensions.Annotated[
        SiacoinOutputId, FieldMetadata(alias="parentID"), pydantic.Field(alias="parentID")
    ]
    unlock_conditions: typing_extensions.Annotated[
        UnlockConditions, FieldMetadata(alias="unlockConditions"), pydantic.Field(alias="unlockConditions")
    ]
    address: Address

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
