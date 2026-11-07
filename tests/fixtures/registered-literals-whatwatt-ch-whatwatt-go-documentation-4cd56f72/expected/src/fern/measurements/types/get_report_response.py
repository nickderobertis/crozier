

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_report_response_meter import GetReportResponseMeter
from .get_report_response_report import GetReportResponseReport
from .get_report_response_system import GetReportResponseSystem


class GetReportResponse(UniversalBaseModel):
    report: typing.Optional[GetReportResponseReport] = None
    meter: typing.Optional[GetReportResponseMeter] = None
    system: typing.Optional[GetReportResponseSystem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
