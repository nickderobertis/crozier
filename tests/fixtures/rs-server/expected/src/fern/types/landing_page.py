

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .landing_page_type import LandingPageType
from .stac_pydantic_api_links_links import StacPydanticApiLinksLinks


class LandingPage(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/core
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/ogcapi-features#landing-page-
    https://github.com/radiantearth/stac-api-spec/tree/v1.0.0/item-search#link-relations
    """

    id: str
    description: str
    stac_version: typing.Optional[str] = None
    links: StacPydanticApiLinksLinks
    stac_extensions: typing.Optional[typing.List[str]] = None
    title: typing.Optional[str] = None
    type: LandingPageType
    conforms_to: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="conformsTo"), pydantic.Field(alias="conformsTo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
