

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_icon_sequence_definition import (
    DestinyDefinitionsCommonDestinyIconSequenceDefinition,
)


class DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition(UniversalBaseModel):
    description: typing.Optional[str] = None
    display_units_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayUnitsName")] = (
        pydantic.Field(default=None)
    )
    """
    When progressions show your "experience" gained, that bar has units (i.e. "Experience", "Bad Dudes Snuffed Out", whatever). This is the localized string for that unit of measurement.
    """

    has_icon: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hasIcon")] = None
    high_res_icon: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="highResIcon")] = (
        pydantic.Field(default=None)
    )
    """
    If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.
    But usually, it will be a small square image that you can use as... well, an icon.
    They are currently represented as 96px x 96px images.
    """

    icon_sequences: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsCommonDestinyIconSequenceDefinition]],
        FieldMetadata(alias="iconSequences"),
    ] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
