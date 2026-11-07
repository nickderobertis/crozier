

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .report_row_container import ReportRowContainer


class StreamDataFetchResult(UniversalBaseModel):
    point_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pointTime"), pydantic.Field(alias="pointTime")
    ] = None
    offset: typing.Optional[int] = None
    page_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")
    ] = None
    last_row_index_position: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="lastRowIndexPosition"), pydantic.Field(alias="lastRowIndexPosition")
    ] = None
    rows: typing.Optional[typing.List[ReportRowContainer]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
