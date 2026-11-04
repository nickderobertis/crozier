

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .period_parameter_editor_time_range_components_item import PeriodParameterEditorTimeRangeComponentsItem


class PeriodParameterEditor(UniversalBaseModel):
    time_range_components: typing_extensions.Annotated[
        typing.Optional[typing.List[PeriodParameterEditorTimeRangeComponentsItem]],
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
