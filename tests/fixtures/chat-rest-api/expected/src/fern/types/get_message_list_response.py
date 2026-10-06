

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message import Message


class GetMessageListResponse(UniversalBaseModel):
    messages: typing.Optional[typing.List[Message]] = None
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ] = None
    page_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageCount"), pydantic.Field(alias="pageCount")
    ] = None
    current_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentPage"), pydantic.Field(alias="currentPage")
    ] = None
    per_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="perPage"), pydantic.Field(alias="perPage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
