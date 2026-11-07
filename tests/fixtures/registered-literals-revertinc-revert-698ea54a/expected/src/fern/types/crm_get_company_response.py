

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_company import CommonCompany
from .common_response_status import CommonResponseStatus


class CrmGetCompanyResponse(UniversalBaseModel):
    status: CommonResponseStatus
    result: CommonCompany

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
