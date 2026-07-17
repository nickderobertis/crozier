

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Token(UniversalBaseModel):
    """
    Token
    """

    id: typing_extensions.Annotated[
        str, FieldMetadata(alias="$id"), pydantic.Field(alias="$id", description="Token ID.")
    ]
    """
    Token ID.
    """

    expire: int = pydantic.Field()
    """
    Token expiration date in Unix timestamp.
    """

    secret: str = pydantic.Field()
    """
    Token secret key. This will return an empty string unless the response is returned using an API key or as part of a webhook payload.
    """

    user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId", description="User ID.")
    ]
    """
    User ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
