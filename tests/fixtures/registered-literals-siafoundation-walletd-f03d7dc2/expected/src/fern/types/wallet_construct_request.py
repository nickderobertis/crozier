

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .siacoin_output import SiacoinOutput
from .siafund_output import SiafundOutput


class WalletConstructRequest(UniversalBaseModel):
    siacoins: typing.Optional[typing.List[SiacoinOutput]] = None
    siafunds: typing.Optional[typing.List[SiafundOutput]] = None
    change_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="changeAddress"), pydantic.Field(alias="changeAddress")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
