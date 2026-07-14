

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_tag_group_response_tag_group import UpdateTagGroupResponseTagGroup


class UpdateTagGroupResponse(UniversalBaseModel):
    success: typing.Optional[str] = None
    tag_group: typing.Optional[UpdateTagGroupResponseTagGroup] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
