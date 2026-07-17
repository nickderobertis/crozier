

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .avatar import Avatar


class LabelUser(UniversalBaseModel):
    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The current avatar of the user.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the user. 000 stands for "unknown"
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name to be displayed for this user, as it was given on the request.
    """

    public_nick_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current nickname of the user.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="The public UUID of the label-user."),
    ] = None
    """
    The public UUID of the label-user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
