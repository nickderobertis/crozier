

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetTokensAddressResponseImpersonates(UniversalBaseModel):
    symbol: typing.Optional[str] = None
    name: typing.Optional[str] = None
    address: typing.Optional[str] = None
    registry_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="registryUrl"), pydantic.Field(alias="registryUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
