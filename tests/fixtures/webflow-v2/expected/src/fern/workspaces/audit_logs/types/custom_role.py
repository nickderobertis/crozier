

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class CustomRole(UniversalBaseModel):
    role_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="roleName"),
        pydantic.Field(alias="roleName", description="The name of the custom role"),
    ] = None
    """
    The name of the custom role
    """

    previous_role_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previousRoleName"),
        pydantic.Field(alias="previousRoleName", description="The previous name of the custom role"),
    ] = None
    """
    The previous name of the custom role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
