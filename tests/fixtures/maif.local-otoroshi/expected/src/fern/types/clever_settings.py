

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CleverSettings(UniversalBaseModel):
    """
    Configuration for CleverCloud client
    """

    consumer_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="consumerKey"),
        pydantic.Field(alias="consumerKey", description="CleverCloud consumer key"),
    ]
    """
    CleverCloud consumer key
    """

    consumer_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="consumerSecret"),
        pydantic.Field(alias="consumerSecret", description="CleverCloud consumer token"),
    ]
    """
    CleverCloud consumer token
    """

    orga_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orgaId"), pydantic.Field(alias="orgaId", description="CleverCloud organization id")
    ]
    """
    CleverCloud organization id
    """

    secret: str = pydantic.Field()
    """
    CleverCloud oauth secret
    """

    token: str = pydantic.Field()
    """
    CleverCloud oauth token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
