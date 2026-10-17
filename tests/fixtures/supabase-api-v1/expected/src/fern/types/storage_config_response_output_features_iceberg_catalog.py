

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StorageConfigResponseOutputFeaturesIcebergCatalog(UniversalBaseModel):
    enabled: bool
    max_namespaces: typing_extensions.Annotated[
        int, FieldMetadata(alias="maxNamespaces"), pydantic.Field(alias="maxNamespaces")
    ]
    max_tables: typing_extensions.Annotated[int, FieldMetadata(alias="maxTables"), pydantic.Field(alias="maxTables")]
    max_catalogs: typing_extensions.Annotated[
        int, FieldMetadata(alias="maxCatalogs"), pydantic.Field(alias="maxCatalogs")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
