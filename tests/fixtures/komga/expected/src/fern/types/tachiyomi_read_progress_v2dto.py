

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TachiyomiReadProgressV2Dto(UniversalBaseModel):
    books_count: typing_extensions.Annotated[int, FieldMetadata(alias="booksCount"), pydantic.Field(alias="booksCount")]
    books_in_progress_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="booksInProgressCount"), pydantic.Field(alias="booksInProgressCount")
    ]
    books_read_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="booksReadCount"), pydantic.Field(alias="booksReadCount")
    ]
    books_unread_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="booksUnreadCount"), pydantic.Field(alias="booksUnreadCount")
    ]
    last_read_continuous_number_sort: typing_extensions.Annotated[
        float, FieldMetadata(alias="lastReadContinuousNumberSort"), pydantic.Field(alias="lastReadContinuousNumberSort")
    ]
    max_number_sort: typing_extensions.Annotated[
        float, FieldMetadata(alias="maxNumberSort"), pydantic.Field(alias="maxNumberSort")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
