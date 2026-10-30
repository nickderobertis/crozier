

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserInfo(UniversalBaseModel):
    user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId", description="The external user ID")
    ]
    """
    The external user ID
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The timestamp when the user was created"),
    ]
    """
    The timestamp when the user was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
