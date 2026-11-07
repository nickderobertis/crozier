

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountSummaryAisItemRolePermissions(UniversalBaseModel):
    can_read: typing_extensions.Annotated[bool, FieldMetadata(alias="canRead"), pydantic.Field(alias="canRead")]
    can_act: typing_extensions.Annotated[bool, FieldMetadata(alias="canAct"), pydantic.Field(alias="canAct")]
    can_host: typing_extensions.Annotated[bool, FieldMetadata(alias="canHost"), pydantic.Field(alias="canHost")]
    can_read_wallet: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canReadWallet"), pydantic.Field(alias="canReadWallet")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
