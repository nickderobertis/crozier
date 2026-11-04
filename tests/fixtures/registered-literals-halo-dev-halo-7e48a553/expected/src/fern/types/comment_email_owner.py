

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommentEmailOwner(UniversalBaseModel):
    """
    Guest/email owner information used when a comment is not owned by a Halo user.
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    Avatar URL of the guest commenter.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name of the guest commenter."),
    ]
    """
    Display name of the guest commenter.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the guest commenter. It is used as the owner name when present.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    Website URL of the guest commenter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
