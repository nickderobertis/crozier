

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetaTagSettings(UniversalBaseModel):
    description: typing.Optional[str] = None
    description_category_page: typing.Optional[str] = None
    description_collection_page: typing.Optional[str] = None
    description_listing_page: typing.Optional[str] = None
    keywords: typing.Optional[str] = None
    title: typing.Optional[str] = None
    title_postfix: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
