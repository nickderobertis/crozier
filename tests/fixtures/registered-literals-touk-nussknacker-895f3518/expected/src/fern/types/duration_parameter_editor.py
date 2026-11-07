

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .duration_parameter_editor_time_range_components_item import DurationParameterEditorTimeRangeComponentsItem


class DurationParameterEditor(UniversalBaseModel):
    time_range_components: typing_extensions.Annotated[
        typing.Optional[typing.List[DurationParameterEditorTimeRangeComponentsItem]],
        FieldMetadata(alias="timeRangeComponents"),
        pydantic.Field(alias="timeRangeComponents"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
