

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReportEnvelopeReportVolumeItem(UniversalBaseModel):
    bus: typing.Optional[int] = None
    meter_id: typing.Optional[str] = None
    date_time: typing.Optional[str] = None
    cumulative: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
