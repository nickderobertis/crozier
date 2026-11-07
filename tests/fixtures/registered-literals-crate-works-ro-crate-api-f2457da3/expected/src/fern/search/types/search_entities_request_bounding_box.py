

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .search_entities_request_bounding_box_bottom_left import SearchEntitiesRequestBoundingBoxBottomLeft
from .search_entities_request_bounding_box_top_right import SearchEntitiesRequestBoundingBoxTopRight


class SearchEntitiesRequestBoundingBox(UniversalBaseModel):
    """
    Will filter the results to entities that exist inside the bounding box.
    """

    top_right: typing_extensions.Annotated[
        SearchEntitiesRequestBoundingBoxTopRight, FieldMetadata(alias="topRight"), pydantic.Field(alias="topRight")
    ]
    bottom_left: typing_extensions.Annotated[
        SearchEntitiesRequestBoundingBoxBottomLeft,
        FieldMetadata(alias="bottomLeft"),
        pydantic.Field(alias="bottomLeft"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
