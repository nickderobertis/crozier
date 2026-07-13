

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .interpolation_interpolation_point import InterpolationInterpolationPoint


class DestinyDefinitionsDestinyStatDisplayDefinition(UniversalBaseModel):
    """
    Describes the way that an Item Stat (see DestinyStatDefinition) is transformed using the DestinyStatGroupDefinition related to that item. See both of the aforementioned definitions for more information about the stages of stat transformation.
    This represents the transformation of a stat into a "Display" stat (the closest value that BNet can get to the in-game display value of the stat)
    """

    display_as_numeric: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="displayAsNumeric")] = (
        pydantic.Field(default=None)
    )
    """
    If this is true, the stat should be displayed as a number. Otherwise, display it as a progress bar. Or, you know, do whatever you want. There's no displayAsNumeric police.
    """

    display_interpolation: typing_extensions.Annotated[
        typing.Optional[typing.List[InterpolationInterpolationPoint]], FieldMetadata(alias="displayInterpolation")
    ] = pydantic.Field(default=None)
    """
    The interpolation table representing how the Investment Stat is transformed into a Display Stat. 
    See DestinyStatDefinition for a description of the stages of stat transformation.
    """

    maximum_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maximumValue")] = (
        pydantic.Field(default=None)
    )
    """
    Regardless of the output of interpolation, this is the maximum possible value that the stat can be. It should also be used as the upper bound for displaying the stat as a progress bar (the minimum always being 0)
    """

    stat_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="statHash")] = pydantic.Field(
        default=None
    )
    """
    The hash identifier for the stat being transformed into a Display stat.
    Use it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition's stats property.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
