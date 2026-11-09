

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_lead import CommonLead
from .common_response_status import CommonResponseStatus


class CrmSearchLeadsResponse(UniversalBaseModel):
    status: CommonResponseStatus
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.List[CommonLead]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
