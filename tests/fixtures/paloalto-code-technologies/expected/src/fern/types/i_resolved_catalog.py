

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .catalog_category import CatalogCategory
from .catalog_group import CatalogGroup
from .catalog_name import CatalogName
from .i_resolved_source import IResolvedSource


class IResolvedCatalog(UniversalBaseModel):
    category: CatalogCategory
    description: str
    first_seen: typing_extensions.Annotated[float, FieldMetadata(alias="firstSeen"), pydantic.Field(alias="firstSeen")]
    group: CatalogGroup
    last_seen: typing_extensions.Annotated[float, FieldMetadata(alias="lastSeen"), pydantic.Field(alias="lastSeen")]
    last_updated: typing_extensions.Annotated[
        float, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    name: CatalogName
    sources: typing.List[IResolvedSource]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
