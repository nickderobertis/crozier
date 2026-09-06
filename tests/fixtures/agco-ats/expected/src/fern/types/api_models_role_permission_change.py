

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_models_role_permission_change_action import ApiModelsRolePermissionChangeAction


class ApiModelsRolePermissionChange(UniversalBaseModel):
    """
    Change to the Permissions that a Role is given.
    """

    action: typing_extensions.Annotated[
        ApiModelsRolePermissionChangeAction,
        FieldMetadata(alias="Action"),
        pydantic.Field(alias="Action", description="The action to take."),
    ]
    """
    The action to take.
    """

    permission: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Permission"),
        pydantic.Field(alias="Permission", description="The name of the permission to grant or revoke."),
    ]
    """
    The name of the permission to grant or revoke.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
