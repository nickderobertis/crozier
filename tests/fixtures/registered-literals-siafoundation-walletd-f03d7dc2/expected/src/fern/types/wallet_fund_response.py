

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chain_index import ChainIndex
from .hash256 import Hash256
from .transaction import Transaction


class WalletFundResponse(UniversalBaseModel):
    basis: ChainIndex
    transaction: Transaction
    to_sign: typing_extensions.Annotated[
        typing.List[Hash256], FieldMetadata(alias="toSign"), pydantic.Field(alias="toSign")
    ]
    depends_on: typing_extensions.Annotated[
        typing.List[Transaction], FieldMetadata(alias="dependsOn"), pydantic.Field(alias="dependsOn")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
