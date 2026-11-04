

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .widget_preset_id import WidgetPresetId
from .widget_provider import WidgetProvider


class Widget(UniversalBaseModel):
    provider: WidgetProvider
    preset_id: typing_extensions.Annotated[
        typing.Optional[WidgetPresetId], FieldMetadata(alias="presetId"), pydantic.Field(alias="presetId")
    ] = None
    config_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="configVersion"), pydantic.Field(alias="configVersion")
    ]
    author_configuration: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="authorConfiguration"),
        pydantic.Field(
            alias="authorConfiguration",
            description="Author-facing App settings before managed-resource IDs are injected.",
        ),
    ] = None
    """
    Author-facing App settings before managed-resource IDs are injected.
    """

    managed_data_source_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="managedDataSourceId"),
        pydantic.Field(
            alias="managedDataSourceId",
            description="Explicit ownership link for a catalog App's hidden managed Data Source.",
        ),
    ] = None
    """
    Explicit ownership link for a catalog App's hidden managed Data Source.
    """

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
