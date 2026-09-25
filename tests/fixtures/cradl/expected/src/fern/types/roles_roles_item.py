

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .roles_roles_item_permissions_item import RolesRolesItemPermissionsItem


class RolesRolesItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    role_id: typing_extensions.Annotated[str, FieldMetadata(alias="roleId"), pydantic.Field(alias="roleId")]
    permissions: typing.List[RolesRolesItemPermissionsItem]
    name: typing.Optional[str] = None
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
