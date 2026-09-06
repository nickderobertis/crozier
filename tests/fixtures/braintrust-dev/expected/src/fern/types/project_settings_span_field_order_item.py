

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_settings_span_field_order_item_layout import ProjectSettingsSpanFieldOrderItemLayout


class ProjectSettingsSpanFieldOrderItem(UniversalBaseModel):
    object_type: str
    column_id: str
    position: str
    layout: typing.Optional[ProjectSettingsSpanFieldOrderItemLayout] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
