

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemGearsetBlockDefinition(UniversalBaseModel):
    """
    If an item has a related gearset, this is the list of items in that set, and an unlock expression that evaluates to a number representing the progress toward gearset completion (a very rare use for unlock expressions!)
    """

    item_list: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="itemList")] = (
        pydantic.Field(default=None)
    )
    """
    The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set.
    """

    tracking_value_max: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="trackingValueMax")] = (
        pydantic.Field(default=None)
    )
    """
    The maximum possible number of items that can be collected.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
