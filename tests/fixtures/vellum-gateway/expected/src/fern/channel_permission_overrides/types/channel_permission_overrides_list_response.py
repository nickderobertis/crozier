

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_overrides_list_response_cells_item import ChannelPermissionOverridesListResponseCellsItem


class ChannelPermissionOverridesListResponse(UniversalBaseModel):
    cells: typing.List[ChannelPermissionOverridesListResponseCellsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
