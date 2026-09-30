

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otel_exporter_config_headers_item import OtelExporterConfigHeadersItem
from .otel_exporter_config_protocol import OtelExporterConfigProtocol
from .otel_exporter_config_traces_propagators_item import OtelExporterConfigTracesPropagatorsItem
from .otel_name_value import OtelNameValue


class OtelExporterConfig(UniversalBaseModel):
    headers: typing.Optional[typing.List[OtelExporterConfigHeadersItem]] = pydantic.Field(default=None)
    """
    Key-value pairs to be used as headers to send with an export request.
    """

    otlp_logs_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target URL to which the exporter is going to send logs. No default.
    """

    otlp_metrics_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target URL to which the exporter is going to send metrics. No default.
    """

    otlp_traces_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Target URL to which the exporter is going to send traces. No default.
    """

    protocol: typing.Optional[OtelExporterConfigProtocol] = pydantic.Field(default=None)
    """
    The transport protocol
    Possible protocol to use with OTLP. Currently, only http/protobuf is supported.
    """

    resource_attributes: typing.Optional[typing.List[OtelNameValue]] = pydantic.Field(default=None)
    """
    Attributes to send as the resource attributes of an export request. We currently only support string-valued attributes.
    """

    traces_propagators: typing.Optional[typing.List[OtelExporterConfigTracesPropagatorsItem]] = pydantic.Field(
        default=None
    )
    """
    List of propagators to inject and extract traces data from headers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
