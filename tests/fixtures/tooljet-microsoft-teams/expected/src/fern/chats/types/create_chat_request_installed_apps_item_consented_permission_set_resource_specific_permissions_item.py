

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateChatRequestInstalledAppsItemConsentedPermissionSetResourceSpecificPermissionsItem(UniversalBaseModel):
    permission_value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="permissionValue"), pydantic.Field(alias="permissionValue")
    ] = None
    permission_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="permissionType"), pydantic.Field(alias="permissionType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
