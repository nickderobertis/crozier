

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .i_resolved_catalog import IResolvedCatalog


class IScan(UniversalBaseModel):
    id: str
    last_cleared: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastCleared"), pydantic.Field(alias="lastCleared")
    ] = None
    last_scan: typing_extensions.Annotated[float, FieldMetadata(alias="lastScan"), pydantic.Field(alias="lastScan")]
    last_updated: typing_extensions.Annotated[
        float, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    results: typing.List[IResolvedCatalog]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
