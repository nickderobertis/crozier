

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_group_response_basic_group import CreateGroupResponseBasicGroup


class CreateGroupResponse(UniversalBaseModel):
    basic_group: CreateGroupResponseBasicGroup

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
