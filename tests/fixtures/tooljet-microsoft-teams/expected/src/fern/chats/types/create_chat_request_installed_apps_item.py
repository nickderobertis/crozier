

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_chat_request_installed_apps_item_consented_permission_set import (
    CreateChatRequestInstalledAppsItemConsentedPermissionSet,
)


class CreateChatRequestInstalledAppsItem(UniversalBaseModel):
    teams_app_odata_bind: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="teamsApp@odata.bind"), pydantic.Field(alias="teamsApp@odata.bind")
    ] = None
    consented_permission_set: typing_extensions.Annotated[
        typing.Optional[CreateChatRequestInstalledAppsItemConsentedPermissionSet],
        FieldMetadata(alias="consentedPermissionSet"),
        pydantic.Field(alias="consentedPermissionSet"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
