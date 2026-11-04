

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .report_envelope_report_volume_item import ReportEnvelopeReportVolumeItem


class ReportEnvelopeReport(UniversalBaseModel):
    id: typing.Optional[int] = None
    interval: typing.Optional[float] = None
    tariff: typing.Optional[int] = None
    date_time: typing.Optional[dt.datetime] = None
    date_time_local: typing.Optional[str] = None
    date_time_utc: typing.Optional[str] = None
    instantaneous_power: typing.Optional[typing.Dict[str, typing.Any]] = None
    voltage: typing.Optional[typing.Dict[str, float]] = None
    current: typing.Optional[typing.Dict[str, float]] = None
    energy: typing.Optional[typing.Dict[str, typing.Any]] = None
    conv_factor: typing.Optional[float] = None
    volume: typing.Optional[typing.List[ReportEnvelopeReportVolumeItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
