

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyRequestsActionsDestinyInsertPlugsRequestEntry(UniversalBaseModel):
    """
    Represents all of the data related to a single plug to be inserted.
    Note that, while you *can* point to a socket that represents infusion, you will receive an error if you attempt to do so. Come on guys, let's play nice.
    """

    plug_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plugItemHash"),
        pydantic.Field(
            alias="plugItemHash",
            description="Plugs are never instanced (except in infusion). So with the hash alone, we should be able to: 1) Infer whether the player actually needs to have the item, or if it's a reusable plug 2) Perform any operation needed to use the Plug, including removing the plug item and running reward sheets.",
        ),
    ] = None
    """
    Plugs are never instanced (except in infusion). So with the hash alone, we should be able to: 1) Infer whether the player actually needs to have the item, or if it's a reusable plug 2) Perform any operation needed to use the Plug, including removing the plug item and running reward sheets.
    """

    socket_array_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="socketArrayType"),
        pydantic.Field(
            alias="socketArrayType",
            description='This property, combined with the socketIndex, tells us which socket we are referring to (since operations can be performed on both Intrinsic and "default" sockets, and they occupy different arrays in the Inventory Item Definition). I know, I know. Don\'t give me that look.',
        ),
    ] = None
    """
    This property, combined with the socketIndex, tells us which socket we are referring to (since operations can be performed on both Intrinsic and "default" sockets, and they occupy different arrays in the Inventory Item Definition). I know, I know. Don't give me that look.
    """

    socket_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="socketIndex"),
        pydantic.Field(
            alias="socketIndex",
            description="The index into the socket array, which identifies the specific socket being operated on. We also need to know the socketArrayType in order to uniquely identify the socket.\r\nDon't point to or try to insert a plug into an infusion socket. It won't work.",
        ),
    ] = None
    """
    The index into the socket array, which identifies the specific socket being operated on. We also need to know the socketArrayType in order to uniquely identify the socket.
    Don't point to or try to insert a plug into an infusion socket. It won't work.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
