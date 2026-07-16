

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityLoadoutRequirement(UniversalBaseModel):
    allowed_equipped_item_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="allowedEquippedItemHashes"),
        pydantic.Field(alias="allowedEquippedItemHashes"),
    ] = None
    allowed_weapon_sub_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="allowedWeaponSubTypes"),
        pydantic.Field(alias="allowedWeaponSubTypes"),
    ] = None
    equipment_slot_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="equipmentSlotHash"), pydantic.Field(alias="equipmentSlotHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
