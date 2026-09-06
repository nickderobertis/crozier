

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_models_user_role_change_action import ApiModelsUserRoleChangeAction


class ApiModelsUserRoleChange(UniversalBaseModel):
    action: typing_extensions.Annotated[
        ApiModelsUserRoleChangeAction,
        FieldMetadata(alias="Action"),
        pydantic.Field(alias="Action", description="The action to take with the role"),
    ]
    """
    The action to take with the role
    """

    name: typing_extensions.Annotated[
        str, FieldMetadata(alias="Name"), pydantic.Field(alias="Name", description="The name of the role")
    ]
    """
    The name of the role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
