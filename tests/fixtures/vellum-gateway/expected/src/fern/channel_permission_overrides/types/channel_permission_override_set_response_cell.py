

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .channel_permission_override_set_response_cell_contact_type import (
    ChannelPermissionOverrideSetResponseCellContactType,
)
from .channel_permission_override_set_response_cell_selector import ChannelPermissionOverrideSetResponseCellSelector
from .channel_permission_override_set_response_cell_threshold import ChannelPermissionOverrideSetResponseCellThreshold


class ChannelPermissionOverrideSetResponseCell(UniversalBaseModel):
    selector: ChannelPermissionOverrideSetResponseCellSelector
    contact_type: typing_extensions.Annotated[
        ChannelPermissionOverrideSetResponseCellContactType,
        FieldMetadata(alias="contactType"),
        pydantic.Field(alias="contactType"),
    ]
    threshold: ChannelPermissionOverrideSetResponseCellThreshold
    note: typing.Optional[str] = None
    updated_at: typing_extensions.Annotated[float, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
