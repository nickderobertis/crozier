

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Password(UniversalBaseModel):
    user_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="userName"),
        pydantic.Field(
            alias="userName",
            description="The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.",
        ),
    ]
    """
    The name of the target user. The value should start with a letter and can only contain underline, letters and numbers.
    """

    password: str = pydantic.Field()
    """
    The corresponding password to the new user to create. 
    The password must be a string of 8 to 64 characters and must include at least three of the following character types: uppercase letters, lowercase letters, numbers, and special characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
