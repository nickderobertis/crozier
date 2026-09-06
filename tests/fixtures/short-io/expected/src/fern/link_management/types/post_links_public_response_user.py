

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostLinksPublicResponseUser(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Creator user ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Creator name
    """

    email: str = pydantic.Field()
    """
    Creator email
    """

    photo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="photoURL"),
        pydantic.Field(alias="photoURL", description="User photo URL"),
    ] = None
    """
    User photo URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
