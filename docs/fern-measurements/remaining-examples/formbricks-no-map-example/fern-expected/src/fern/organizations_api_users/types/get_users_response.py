

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_users_response_data_item import GetUsersResponseDataItem
from .get_users_response_meta import GetUsersResponseMeta


class GetUsersResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetUsersResponseDataItem]] = None
    meta: typing.Optional[GetUsersResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
