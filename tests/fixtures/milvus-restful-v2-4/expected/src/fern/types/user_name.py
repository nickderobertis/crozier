

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserName(UniversalBaseModel):
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
