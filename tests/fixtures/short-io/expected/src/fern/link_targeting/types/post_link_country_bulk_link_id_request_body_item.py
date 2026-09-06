

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_link_country_bulk_link_id_request_body_item_country import PostLinkCountryBulkLinkIdRequestBodyItemCountry


class PostLinkCountryBulkLinkIdRequestBodyItem(UniversalBaseModel):
    country: PostLinkCountryBulkLinkIdRequestBodyItemCountry = pydantic.Field()
    """
    Country code
    """

    original_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalURL"), pydantic.Field(alias="originalURL")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
