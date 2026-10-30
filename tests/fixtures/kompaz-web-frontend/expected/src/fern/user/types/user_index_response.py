

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class UserIndexResponse(UniversalBaseModel):
    items: str
    page_number: typing_extensions.Annotated[str, FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber")]
    page_size: typing_extensions.Annotated[str, FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")]
    total_count: typing_extensions.Annotated[str, FieldMetadata(alias="totalCount"), pydantic.Field(alias="totalCount")]
    total_pages: typing_extensions.Annotated[int, FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")]
    has_previous_page: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasPreviousPage"), pydantic.Field(alias="hasPreviousPage")
    ]
    has_next_page: typing_extensions.Annotated[
        bool, FieldMetadata(alias="hasNextPage"), pydantic.Field(alias="hasNextPage")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
