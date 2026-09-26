

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WatchEventData(UniversalBaseModel):
    container_host_namespace: typing.Optional[str] = None
    container_hostname: typing.Optional[str] = None
    container_id: typing.Optional[str] = None
    container_qos: typing.Optional[str] = None
    container_type: typing.Optional[str] = None
    hostname: str
    kernel_observed_timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    UTC time when the kernel observed the event, when available, emitted with nine fractional digits.
    """

    observed_timestamp: dt.datetime = pydantic.Field()
    """
    UTC time when the event producer observed the event in userspace, emitted with nine fractional digits.
    """

    region: str
    tracer_id: typing.Optional[str] = None
    tracer_name: typing.Optional[str] = None
    tracer_run_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
