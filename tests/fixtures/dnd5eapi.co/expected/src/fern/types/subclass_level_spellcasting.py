

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SubclassLevelSpellcasting(UniversalBaseModel):
    """
    Summary of spells known at this level.
    """

    cantrips_known: typing.Optional[float] = None
    spell_slots_level1: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_1")
    ] = None
    spell_slots_level2: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_2")
    ] = None
    spell_slots_level3: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_3")
    ] = None
    spell_slots_level4: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_4")
    ] = None
    spell_slots_level5: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_5")
    ] = None
    spell_slots_level6: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_6")
    ] = None
    spell_slots_level7: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_7")
    ] = None
    spell_slots_level8: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_8")
    ] = None
    spell_slots_level9: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="spell_slots_level_9")
    ] = None
    spells_known: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
