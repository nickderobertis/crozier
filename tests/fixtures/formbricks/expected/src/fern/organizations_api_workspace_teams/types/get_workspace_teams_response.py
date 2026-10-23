

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_workspace_teams_response_data_item import GetWorkspaceTeamsResponseDataItem
from .get_workspace_teams_response_meta import GetWorkspaceTeamsResponseMeta


class GetWorkspaceTeamsResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetWorkspaceTeamsResponseDataItem]] = None
    meta: typing.Optional[GetWorkspaceTeamsResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
