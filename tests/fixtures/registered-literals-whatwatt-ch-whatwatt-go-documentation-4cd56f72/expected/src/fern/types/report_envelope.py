

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .report_envelope_meter import ReportEnvelopeMeter
from .report_envelope_report import ReportEnvelopeReport
from .report_envelope_system import ReportEnvelopeSystem


class ReportEnvelope(UniversalBaseModel):
    report: typing.Optional[ReportEnvelopeReport] = None
    meter: typing.Optional[ReportEnvelopeMeter] = None
    system: typing.Optional[ReportEnvelopeSystem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
