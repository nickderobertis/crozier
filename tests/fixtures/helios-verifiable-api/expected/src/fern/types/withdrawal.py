

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .uint64 import Uint64
from .uint256 import Uint256


class Withdrawal(UniversalBaseModel):
    index: Uint64
    validator_index: typing_extensions.Annotated[
        Uint64, FieldMetadata(alias="validatorIndex"), pydantic.Field(alias="validatorIndex")
    ]
    address: Address
    amount: Uint256

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
