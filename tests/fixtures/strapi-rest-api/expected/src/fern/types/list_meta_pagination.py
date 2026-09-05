

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListMetaPagination(UniversalBaseModel):
    """
    Page-based responses include page/pageSize/pageCount/total; offset-based include start/limit/total.
    """

    page: typing.Optional[int] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    page_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageCount"), pydantic.Field(alias="pageCount")
    ] = None
    start: typing.Optional[int] = None
    limit: typing.Optional[int] = None
    total: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
