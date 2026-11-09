

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_stat_data_dto import TimeStatDataDto


class TableOperationStatsDto(UniversalBaseModel):
    operations: typing.Optional[str] = None
    operation_stats: typing_extensions.Annotated[
        typing.Optional[TimeStatDataDto], FieldMetadata(alias="operationStats"), pydantic.Field(alias="operationStats")
    ] = None
    minute_stats: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, TimeStatDataDto]],
        FieldMetadata(alias="minuteStats"),
        pydantic.Field(alias="minuteStats"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
