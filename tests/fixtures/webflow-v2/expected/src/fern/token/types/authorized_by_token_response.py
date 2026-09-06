

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class AuthorizedByTokenResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the user
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address
    """

    first_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="firstName"),
        pydantic.Field(alias="firstName", description="The user's first name"),
    ] = None
    """
    The user's first name
    """

    last_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastName"),
        pydantic.Field(alias="lastName", description="The user's last name"),
    ] = None
    """
    The user's last name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
