

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .role import Role


class UserPermission(UniversalBaseModel):
    """
    Resolved role and permission information for a user.
    """

    permissions: typing.List[Role] = pydantic.Field()
    """
    Role templates or permissions resolved from granted roles.
    """

    roles: typing.List[Role] = pydantic.Field()
    """
    Roles granted to the user.
    """

    ui_permissions: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="uiPermissions"),
        pydantic.Field(alias="uiPermissions", description="Resolved UI permission identifiers."),
    ]
    """
    Resolved UI permission identifiers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
