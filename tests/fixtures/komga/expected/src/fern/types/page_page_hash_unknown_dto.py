

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_hash_unknown_dto import PageHashUnknownDto
from .pageable_object import PageableObject
from .sort_object import SortObject


class PagePageHashUnknownDto(UniversalBaseModel):
    content: typing.Optional[typing.List[PageHashUnknownDto]] = None
    empty: typing.Optional[bool] = None
    first: typing.Optional[bool] = None
    last: typing.Optional[bool] = None
    number: typing.Optional[int] = None
    number_of_elements: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfElements"), pydantic.Field(alias="numberOfElements")
    ] = None
    pageable: typing.Optional[PageableObject] = None
    size: typing.Optional[int] = None
    sort: typing.Optional[SortObject] = None
    total_elements: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalElements"), pydantic.Field(alias="totalElements")
    ] = None
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
