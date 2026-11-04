

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ui_plugin_provider import UiPluginProvider


class UiPluginProviderDescriptor(UniversalBaseModel):
    """
    Browser descriptor for the currently enabled plugin and theme UI providers.
    """

    legacy_script: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="legacyScript"),
        pydantic.Field(
            alias="legacyScript", description="Legacy aggregate script URL, present when a legacy provider exists."
        ),
    ] = None
    """
    Legacy aggregate script URL, present when a legacy provider exists.
    """

    providers: typing.List[UiPluginProvider]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
