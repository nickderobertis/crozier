

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_contact import CommonContact
from .common_response_status import CommonResponseStatus


class CrmGetContactResponse(UniversalBaseModel):
    status: CommonResponseStatus
    result: CommonContact

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
