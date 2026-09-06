

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .report_request_reason import ReportRequestReason


class ReportRequest(UniversalBaseModel):
    reason: ReportRequestReason = pydantic.Field()
    """
    Reason for the report
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional details about the report
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
