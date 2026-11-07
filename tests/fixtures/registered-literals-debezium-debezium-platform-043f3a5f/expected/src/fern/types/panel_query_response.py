

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .time_range import TimeRange
from .time_series import TimeSeries


class PanelQueryResponse(UniversalBaseModel):
    panel_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="panelId"), pydantic.Field(alias="panelId")
    ] = None
    pipeline_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pipelineId"), pydantic.Field(alias="pipelineId")
    ] = None
    time_range: typing_extensions.Annotated[
        typing.Optional[TimeRange], FieldMetadata(alias="timeRange"), pydantic.Field(alias="timeRange")
    ] = None
    series: typing.Optional[typing.List[TimeSeries]] = None
    metadata: typing.Optional[Metadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
