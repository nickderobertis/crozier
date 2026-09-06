

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_link_region_bulk_link_id_request_body_item_country import PostLinkRegionBulkLinkIdRequestBodyItemCountry


class PostLinkRegionBulkLinkIdRequestBodyItem(UniversalBaseModel):
    country: PostLinkRegionBulkLinkIdRequestBodyItemCountry = pydantic.Field()
    """
    Country code
    """

    region: str = pydantic.Field()
    """
    ISO 3166-2 region code
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
