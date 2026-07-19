

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthResponse(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid", description="UUID of the user")
    ]
    """
    UUID of the user
    """

    is_admin: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user is an admin
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
