

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Contributor(UniversalBaseModel):
    """
    User summary for a content owner or contributor.
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    User avatar URL.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="User display name."),
    ] = None
    """
    User display name.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User metadata name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
