

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_chat_request_installed_apps_item_consented_permission_set_resource_specific_permissions_item import (
    CreateChatRequestInstalledAppsItemConsentedPermissionSetResourceSpecificPermissionsItem,
)


class CreateChatRequestInstalledAppsItemConsentedPermissionSet(UniversalBaseModel):
    resource_specific_permissions: typing_extensions.Annotated[
        typing.Optional[
            typing.List[CreateChatRequestInstalledAppsItemConsentedPermissionSetResourceSpecificPermissionsItem]
        ],
        FieldMetadata(alias="resourceSpecificPermissions"),
        pydantic.Field(alias="resourceSpecificPermissions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
