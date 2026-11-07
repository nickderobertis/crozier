

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_response_status import CommonResponseStatus
from .common_user import CommonUser


class CrmSearchUsersResponse(UniversalBaseModel):
    status: CommonResponseStatus
    results: typing.List[CommonUser]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
