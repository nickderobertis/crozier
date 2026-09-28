

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_override_set_response_cell import ChannelPermissionOverrideSetResponseCell


class ChannelPermissionOverrideSetResponse(UniversalBaseModel):
    cell: ChannelPermissionOverrideSetResponseCell

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
