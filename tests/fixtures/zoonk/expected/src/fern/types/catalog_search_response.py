

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_search_response_chapters_item import CatalogSearchResponseChaptersItem
from .catalog_search_response_courses_item import CatalogSearchResponseCoursesItem


class CatalogSearchResponse(UniversalBaseModel):
    chapters: typing.List[CatalogSearchResponseChaptersItem]
    courses: typing.List[CatalogSearchResponseCoursesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
