

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyNodeSocketReplaceResponse(UniversalBaseModel):
    """
    This is a bit of an odd duck. Apparently, if talent nodes steps have this data, the game will go through on step activation and alter the first Socket it finds on the item that has a type matching the given socket type, inserting the indicated plug item.
    """

    plug_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plugItemHash"),
        pydantic.Field(
            alias="plugItemHash",
            description="The hash identifier of the plug item that will be inserted into the socket found.",
        ),
    ] = None
    """
    The hash identifier of the plug item that will be inserted into the socket found.
    """

    socket_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="socketTypeHash"),
        pydantic.Field(
            alias="socketTypeHash",
            description="The hash identifier of the socket type to find amidst the item's sockets (the item to which this talent grid is attached). See DestinyInventoryItemDefinition.sockets.socketEntries to find the socket type of sockets on the item in question.",
        ),
    ] = None
    """
    The hash identifier of the socket type to find amidst the item's sockets (the item to which this talent grid is attached). See DestinyInventoryItemDefinition.sockets.socketEntries to find the socket type of sockets on the item in question.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
