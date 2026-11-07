

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .catalog_plugin_category import CatalogPluginCategory
from .plugin_attention import PluginAttention
from .plugin_requirement import PluginRequirement


class CatalogPlugin(UniversalBaseModel):
    id: str
    version: int = pydantic.Field()
    """
    Definition contract version compiled into this release
    """

    name: str
    description: str
    category: CatalogPluginCategory
    icon: str = pydantic.Field()
    """
    Bounded icon identifier; unknown values render a generic icon
    """

    management_path: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="managementPath"),
        pydantic.Field(alias="managementPath", description="Studio route; a navigation hint"),
    ]
    """
    Studio route; a navigation hint
    """

    instance_noun_singular: typing_extensions.Annotated[
        str, FieldMetadata(alias="instanceNounSingular"), pydantic.Field(alias="instanceNounSingular")
    ]
    instance_noun_plural: typing_extensions.Annotated[
        str, FieldMetadata(alias="instanceNounPlural"), pydantic.Field(alias="instanceNounPlural")
    ]
    requirements: typing.List[PluginRequirement]
    capabilities: typing.List[str]
    documentation: typing.Optional[str] = None
    installed: bool
    installable: bool
    configured: bool
    active: bool
    instance_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="instanceCount"), pydantic.Field(alias="instanceCount")
    ]
    attention: typing.List[PluginAttention]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
