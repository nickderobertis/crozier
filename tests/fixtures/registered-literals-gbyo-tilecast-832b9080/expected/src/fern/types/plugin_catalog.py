

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .catalog_plugin import CatalogPlugin
from .plugin_catalog_unsupported_installations_item import PluginCatalogUnsupportedInstallationsItem


class PluginCatalog(UniversalBaseModel):
    items: typing.List[CatalogPlugin]
    unsupported_installations: typing_extensions.Annotated[
        typing.List[PluginCatalogUnsupportedInstallationsItem],
        FieldMetadata(alias="unsupportedInstallations"),
        pydantic.Field(
            alias="unsupportedInstallations",
            description="Installation rows naming plugins this release does not know. Preserved and inert.",
        ),
    ]
    """
    Installation rows naming plugins this release does not know. Preserved and inert.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
