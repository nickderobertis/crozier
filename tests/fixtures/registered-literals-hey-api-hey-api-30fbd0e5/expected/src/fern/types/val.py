

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .val_author import ValAuthor
from .val_links import ValLinks
from .val_privacy import ValPrivacy


class Val(UniversalBaseModel):
    """
    A Val
    """

    name: str
    id: str = pydantic.Field()
    """
    The id of the val
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    privacy: ValPrivacy = pydantic.Field()
    """
    This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.
    """

    author: ValAuthor
    image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imageUrl"),
        pydantic.Field(alias="imageUrl", description="The URL of this val's image"),
    ] = None
    """
    The URL of this val's image
    """

    description: typing.Optional[str] = None
    links: ValLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
