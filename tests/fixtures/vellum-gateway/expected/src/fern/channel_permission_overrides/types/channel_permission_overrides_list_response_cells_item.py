

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_permission_overrides_list_response_cells_item_contact_type import (
    ChannelPermissionOverridesListResponseCellsItemContactType,
)
from .channel_permission_overrides_list_response_cells_item_selector import (
    ChannelPermissionOverridesListResponseCellsItemSelector,
)
from .channel_permission_overrides_list_response_cells_item_threshold import (
    ChannelPermissionOverridesListResponseCellsItemThreshold,
)


class ChannelPermissionOverridesListResponseCellsItem(UniversalBaseModel):
    selector: ChannelPermissionOverridesListResponseCellsItemSelector
    contact_type: typing_extensions.Annotated[
        ChannelPermissionOverridesListResponseCellsItemContactType,
        FieldMetadata(alias="contactType"),
        pydantic.Field(alias="contactType"),
    ]
    threshold: ChannelPermissionOverridesListResponseCellsItemThreshold
    note: typing.Optional[str] = None
    updated_at: typing_extensions.Annotated[float, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
