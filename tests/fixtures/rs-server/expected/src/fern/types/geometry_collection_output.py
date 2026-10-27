

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class GeometryCollectionOutput(UniversalBaseModel):
    """
    GeometryCollection Model
    """

    bbox: typing.Optional[typing.List[typing.Any]] = None
    geometries: typing.List["GeometryCollectionOutputGeometriesItem"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .geometry_collection_output_geometries_item import GeometryCollectionOutputGeometriesItem

update_forward_refs(
    GeometryCollectionOutput, GeometryCollectionOutputGeometriesItem=GeometryCollectionOutputGeometriesItem
)
