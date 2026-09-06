

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pageable import Pageable


class PaginationProperties(UniversalBaseModel):
    empty: typing.Optional[bool] = None
    number_of_elements: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfElements"), pydantic.Field(alias="numberOfElements")
    ] = None
    offset: typing.Optional[int] = None
    page_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber")
    ] = None
    pageable: typing.Optional[Pageable] = None
    size: typing.Optional[int] = None
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ] = None
    total_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalSize"), pydantic.Field(alias="totalSize")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
