

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stac_pydantic_api_collection_collection import StacPydanticApiCollectionCollection
from .stac_pydantic_api_links_links import StacPydanticApiLinksLinks


class Collections(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/ogcapi-features#endpoints
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/ogcapi-features#collections-collections
    """

    links: StacPydanticApiLinksLinks
    collections: typing.List[StacPydanticApiCollectionCollection]
    number_matched: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberMatched"), pydantic.Field(alias="numberMatched")
    ] = None
    number_returned: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberReturned"), pydantic.Field(alias="numberReturned")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
