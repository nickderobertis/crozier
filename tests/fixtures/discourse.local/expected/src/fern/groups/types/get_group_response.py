

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_group_response_extras import GetGroupResponseExtras
from .get_group_response_group import GetGroupResponseGroup


class GetGroupResponse(UniversalBaseModel):
    extras: GetGroupResponseExtras
    group: GetGroupResponseGroup

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
