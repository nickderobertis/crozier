

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .widget_input_preset_id import WidgetInputPresetId
from .widget_provider import WidgetProvider


class WidgetInput(UniversalBaseModel):
    provider: WidgetProvider
    preset_id: typing_extensions.Annotated[
        typing.Optional[WidgetInputPresetId], FieldMetadata(alias="presetId"), pydantic.Field(alias="presetId")
    ] = None
    name: str
    description: typing.Optional[str] = None
    configuration: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Provider-specific configuration. Native text Widgets omit textScale for automatic bounds-first sizing or use 25–500 percent; contentPadding defaults to 10 percent per edge and accepts 0–40.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
