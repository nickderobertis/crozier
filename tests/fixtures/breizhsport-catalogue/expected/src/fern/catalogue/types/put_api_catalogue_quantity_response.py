

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_api_catalogue_quantity_response_articles_item import PutApiCatalogueQuantityResponseArticlesItem


class PutApiCatalogueQuantityResponse(UniversalBaseModel):
    message: typing.Optional[str] = None
    articles: typing.Optional[typing.List[PutApiCatalogueQuantityResponseArticlesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
