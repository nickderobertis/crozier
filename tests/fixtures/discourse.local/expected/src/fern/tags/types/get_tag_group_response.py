

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_tag_group_response_tag_group import GetTagGroupResponseTagGroup


class GetTagGroupResponse(UniversalBaseModel):
    tag_group: typing.Optional[GetTagGroupResponseTagGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
