

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_definitions_common_destiny_position_definition import DestinyDefinitionsCommonDestinyPositionDefinition


class DestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition(UniversalBaseModel):
    """
    These Art Elements are meant to represent one-off visual effects overlaid on the map. Currently, we do not have a pipeline to import the assets for these overlays, so this info exists as a placeholder for when such a pipeline exists (if it ever will)
    """

    position: typing.Optional[DestinyDefinitionsCommonDestinyPositionDefinition] = pydantic.Field(default=None)
    """
    The position on the map of the art element.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
