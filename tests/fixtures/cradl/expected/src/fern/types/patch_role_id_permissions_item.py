

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .patch_role_id_permissions_item_action import PatchRoleIdPermissionsItemAction
from .patch_role_id_permissions_item_effect import PatchRoleIdPermissionsItemEffect


class PatchRoleIdPermissionsItem(UniversalBaseModel):
    resource_id: typing_extensions.Annotated[str, FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")]
    effect: PatchRoleIdPermissionsItemEffect
    action: PatchRoleIdPermissionsItemAction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
