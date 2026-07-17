

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_dye_reference import DestinyDyeReference


class DestinyCharacterDestinyItemPeerView(UniversalBaseModel):
    """
    Bare minimum summary information for an item, for the sake of 3D rendering the item.
    """

    dyes: typing.Optional[typing.List[DestinyDyeReference]] = pydantic.Field(default=None)
    """
    The list of dyes that have been applied to this item.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="The hash identifier of the item in question. Use it to look up the DestinyInventoryItemDefinition of the item for static rendering data.",
        ),
    ] = None
    """
    The hash identifier of the item in question. Use it to look up the DestinyInventoryItemDefinition of the item for static rendering data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
