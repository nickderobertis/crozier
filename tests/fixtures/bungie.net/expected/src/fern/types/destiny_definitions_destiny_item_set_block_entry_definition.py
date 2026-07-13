

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemSetBlockEntryDefinition(UniversalBaseModel):
    """
    Defines a particular entry in an ItemSet (AKA a particular Quest Step in a Quest)
    """

    item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemHash")] = pydantic.Field(
        default=None
    )
    """
    This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step.
    """

    tracking_value: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="trackingValue")] = (
        pydantic.Field(default=None)
    )
    """
    Used for tracking which step a user reached. These values will be populated in the user's internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
