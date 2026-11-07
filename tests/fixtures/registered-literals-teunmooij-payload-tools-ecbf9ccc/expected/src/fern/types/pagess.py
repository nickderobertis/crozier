

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pages import Pages


class Pagess(UniversalBaseModel):
    docs: typing.List[Pages]
    total_docs: typing_extensions.Annotated[float, FieldMetadata(alias="totalDocs"), pydantic.Field(alias="totalDocs")]
    limit: float
    total_pages: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ]
    page: float
    paging_counter: typing_extensions.Annotated[
        float, FieldMetadata(alias="pagingCounter"), pydantic.Field(alias="pagingCounter")
    ]
    has_prev_page: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasPrevPage"), pydantic.Field(alias="hasPrevPage")
    ]
    has_next_page: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasNextPage"), pydantic.Field(alias="hasNextPage")
    ]
    prev_page: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="prevPage"), pydantic.Field(alias="prevPage")
    ] = None
    next_page: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="nextPage"), pydantic.Field(alias="nextPage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
