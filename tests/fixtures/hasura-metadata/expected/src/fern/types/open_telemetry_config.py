

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_telemetry_config_data_types_item import OpenTelemetryConfigDataTypesItem
from .otel_batch_span_processor_config import OtelBatchSpanProcessorConfig
from .otel_exporter_config import OtelExporterConfig


class OpenTelemetryConfig(UniversalBaseModel):
    batch_span_processor: typing.Optional[OtelBatchSpanProcessorConfig] = None
    data_types: typing.Optional[typing.List[OpenTelemetryConfigDataTypesItem]] = None
    exporter_otlp: typing.Optional[OtelExporterConfig] = None
    status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
