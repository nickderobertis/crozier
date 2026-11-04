

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UcUserVo(UniversalBaseModel):
    """
    Masked current user profile. The password hash is never exposed.
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    avatar of the current user
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="display name of the current user"),
    ] = None
    """
    display name of the current user
    """

    name: str = pydantic.Field()
    """
    username of the current user
    """

    password_set: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="passwordSet"),
        pydantic.Field(alias="passwordSet", description="whether the current user has a password set"),
    ]
    """
    whether the current user has a password set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
