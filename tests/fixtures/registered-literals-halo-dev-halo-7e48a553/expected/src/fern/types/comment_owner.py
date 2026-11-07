

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CommentOwner(UniversalBaseModel):
    """
    Identity of a comment or reply owner.
    """

    annotations: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Additional owner metadata, such as avatar, website, or email hash.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the owner."),
    ] = None
    """
    Display name shown for the owner.
    """

    kind: str = pydantic.Field()
    """
    Owner identity kind. Built-in values are User and Email.
    """

    name: str = pydantic.Field()
    """
    Owner identifier. For User owners, this is the User metadata.name; for Email owners, an email address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
