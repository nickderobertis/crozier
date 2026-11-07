

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .spend_policy import SpendPolicy


class WalletAddress(UniversalBaseModel):
    address: Address
    description: str
    spend_policy: typing_extensions.Annotated[
        typing.Optional[SpendPolicy], FieldMetadata(alias="spendPolicy"), pydantic.Field(alias="spendPolicy")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
