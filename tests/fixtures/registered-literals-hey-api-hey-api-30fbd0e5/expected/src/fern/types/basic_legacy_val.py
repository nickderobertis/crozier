

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .basic_legacy_val_author import BasicLegacyValAuthor
from .basic_legacy_val_links import BasicLegacyValLinks
from .basic_legacy_val_privacy import BasicLegacyValPrivacy
from .basic_legacy_val_type import BasicLegacyValType


class BasicLegacyVal(UniversalBaseModel):
    """
    A Val
    """

    name: str = pydantic.Field()
    """
    The name of this val
    """

    id: str = pydantic.Field()
    """
    This val's id
    """

    version: int = pydantic.Field()
    """
    The version of this val, starting at zero
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    TypeScript code associated with this val
    """

    public: bool = pydantic.Field()
    """
    Whether this val is available publicly on Val Town
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    privacy: BasicLegacyValPrivacy = pydantic.Field()
    """
    This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.
    """

    type: BasicLegacyValType = pydantic.Field()
    """
    The type of a val. HTTP can receive web requests, Email can receive emails, Cron runs periodically, and Script can be used for libraries or one-off calculations
    """

    url: str = pydantic.Field()
    """
    The URL of this resource on the Val Town website
    """

    links: BasicLegacyValLinks
    author: typing.Optional[BasicLegacyValAuthor] = pydantic.Field(default=None)
    """
    The user who created this val
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
