

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sort_object import SortObject


class PageableObject(UniversalBaseModel):
    offset: typing.Optional[int] = None
    page_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber")
    ] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    paged: typing.Optional[bool] = None
    sort: typing.Optional[SortObject] = None
    unpaged: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
