

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tab_links import TabLinks
from .way_points_embedded import WayPointsEmbedded


class WayPoints(UniversalBaseModel):
    embedded: typing_extensions.Annotated[
        typing.Optional[WayPointsEmbedded], FieldMetadata(alias="_embedded"), pydantic.Field(alias="_embedded")
    ] = None
    links: typing_extensions.Annotated[TabLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    total: int
    total_page: typing_extensions.Annotated[int, FieldMetadata(alias="totalPage"), pydantic.Field(alias="totalPage")]
    current_page: typing_extensions.Annotated[
        int, FieldMetadata(alias="currentPage"), pydantic.Field(alias="currentPage")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
