

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pagination_links import PaginationLinks


class Pagination(UniversalBaseModel):
    per_page: typing_extensions.Annotated[float, FieldMetadata(alias="perPage"), pydantic.Field(alias="perPage")]
    page_count: typing_extensions.Annotated[float, FieldMetadata(alias="pageCount"), pydantic.Field(alias="pageCount")]
    links: PaginationLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
