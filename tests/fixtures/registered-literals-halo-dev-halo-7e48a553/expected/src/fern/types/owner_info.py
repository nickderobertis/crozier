

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OwnerInfo(UniversalBaseModel):
    """
    Resolved owner summary for a comment or reply.
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    Owner avatar URL.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Owner display name."),
    ] = None
    """
    Owner display name.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Owner email address when available.
    """

    kind: typing.Optional[str] = pydantic.Field(default=None)
    """
    Owner kind, such as User or email.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Owner name. For Halo users, this is the user metadata name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
