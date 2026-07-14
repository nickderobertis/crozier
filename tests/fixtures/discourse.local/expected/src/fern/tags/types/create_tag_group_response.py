

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_tag_group_response_tag_group import CreateTagGroupResponseTagGroup


class CreateTagGroupResponse(UniversalBaseModel):
    tag_group: CreateTagGroupResponseTagGroup

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
