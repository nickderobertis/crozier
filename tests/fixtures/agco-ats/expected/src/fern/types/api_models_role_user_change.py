

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_models_role_user_change_action import ApiModelsRoleUserChangeAction


class ApiModelsRoleUserChange(UniversalBaseModel):
    action: typing_extensions.Annotated[
        ApiModelsRoleUserChangeAction,
        FieldMetadata(alias="Action"),
        pydantic.Field(alias="Action", description="The action to take with the user"),
    ]
    """
    The action to take with the user
    """

    id: typing_extensions.Annotated[
        int, FieldMetadata(alias="Id"), pydantic.Field(alias="Id", description="The Id of the User")
    ]
    """
    The Id of the User
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
