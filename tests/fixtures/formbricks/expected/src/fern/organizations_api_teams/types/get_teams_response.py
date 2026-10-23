

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_teams_response_data_item import GetTeamsResponseDataItem
from .get_teams_response_meta import GetTeamsResponseMeta


class GetTeamsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetTeamsResponseDataItem]] = None
    meta: typing.Optional[GetTeamsResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
