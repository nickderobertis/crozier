

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_roles_permissions_item_action import PostRolesPermissionsItemAction
from .post_roles_permissions_item_effect import PostRolesPermissionsItemEffect


class PostRolesPermissionsItem(UniversalBaseModel):
    resource_id: typing_extensions.Annotated[str, FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")]
    effect: PostRolesPermissionsItemEffect
    action: PostRolesPermissionsItemAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
