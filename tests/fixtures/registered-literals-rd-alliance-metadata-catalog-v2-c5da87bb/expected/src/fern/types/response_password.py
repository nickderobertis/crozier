

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ResponsePassword(UniversalBaseModel):
    api_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")
    ] = None
    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    Confirmation of the username for which the password was reset.
    """

    password_reset: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the reset was successful, false otherwise.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
