

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .byte import Byte
from .uint import Uint
from .uint256 import Uint256


class AuthorizationListItem(UniversalBaseModel):
    chain_id: typing_extensions.Annotated[
        Uint,
        FieldMetadata(alias="chainId"),
        pydantic.Field(alias="chainId", description="Chain ID on which this transaction is valid"),
    ]
    """
    Chain ID on which this transaction is valid
    """

    nonce: Uint
    address: Address
    y_parity: typing_extensions.Annotated[
        Byte,
        FieldMetadata(alias="yParity"),
        pydantic.Field(
            alias="yParity", description="The parity (0 for even, 1 for odd) of the y-value of the secp256k1 signature"
        ),
    ]
    """
    The parity (0 for even, 1 for odd) of the y-value of the secp256k1 signature
    """

    r: Uint256
    s: Uint256

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
