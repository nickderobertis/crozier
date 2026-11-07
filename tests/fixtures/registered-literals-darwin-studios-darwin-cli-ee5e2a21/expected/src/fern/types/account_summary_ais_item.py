

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_summary_ais_item_role import AccountSummaryAisItemRole
from .account_summary_ais_item_role_permissions import AccountSummaryAisItemRolePermissions


class AccountSummaryAisItem(UniversalBaseModel):
    ai_id: typing_extensions.Annotated[str, FieldMetadata(alias="aiId"), pydantic.Field(alias="aiId")]
    type: str
    name: str
    handle: typing.Optional[str] = None
    avatar_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarUrl"), pydantic.Field(alias="avatarUrl")
    ] = None
    description: typing.Optional[str] = None
    visibility: str
    status: str
    role: AccountSummaryAisItemRole
    role_permissions: typing_extensions.Annotated[
        AccountSummaryAisItemRolePermissions,
        FieldMetadata(alias="rolePermissions"),
        pydantic.Field(alias="rolePermissions"),
    ]
    is_active: typing_extensions.Annotated[bool, FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
