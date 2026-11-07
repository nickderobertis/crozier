

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ui_plugin_provider_kind import UiPluginProviderKind
from .ui_plugin_provider_type import UiPluginProviderType


class UiPluginProvider(UniversalBaseModel):
    """
    One ordered UI provider classification.
    """

    entry: typing.Optional[str] = pydantic.Field(default=None)
    """
    ESM entry URL, required for ESM providers.
    """

    kind: UiPluginProviderKind = pydantic.Field()
    """
    Provider classification and loading mode.
    """

    name: str
    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Discovery failure reason, required for invalid providers.
    """

    style: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional startup stylesheet URL.
    """

    type: UiPluginProviderType
    version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
