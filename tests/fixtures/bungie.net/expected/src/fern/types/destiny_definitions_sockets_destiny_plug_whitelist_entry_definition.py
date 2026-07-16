

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition(UniversalBaseModel):
    """
    Defines a plug "Category" that is allowed to be plugged into a socket of this type.
    This should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.
    """

    category_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="categoryHash"),
        pydantic.Field(
            alias="categoryHash",
            description="The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash.\r\nNote that this does NOT relate to any Definition in itself, it is only used for comparison purposes.",
        ),
    ] = None
    """
    The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash.
    Note that this does NOT relate to any Definition in itself, it is only used for comparison purposes.
    """

    category_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="categoryIdentifier"),
        pydantic.Field(
            alias="categoryIdentifier",
            description="The string identifier for the category, which is here mostly for debug purposes.",
        ),
    ] = None
    """
    The string identifier for the category, which is here mostly for debug purposes.
    """

    reinitialization_possible_plug_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="reinitializationPossiblePlugHashes"),
        pydantic.Field(
            alias="reinitializationPossiblePlugHashes",
            description="The list of all plug items (DestinyInventoryItemDefinition) that the socket may randomly be populated with when reinitialized.\r\nWhich ones you should actually show are determined by the plug being inserted into the socket, and the socket’s type.\r\nWhen you inspect the plug that could go into a Masterwork Socket, look up the socket type of the socket being inspected and find the DestinySocketTypeDefinition.\r\nThen, look at the Plugs that can fit in that socket. Find the Whitelist in the DestinySocketTypeDefinition that matches the plug item’s categoryhash.\r\nThat whitelist entry will potentially have a new “reinitializationPossiblePlugHashes” property.If it does, that means we know what it will roll if you try to insert this plug into this socket.",
        ),
    ] = None
    """
    The list of all plug items (DestinyInventoryItemDefinition) that the socket may randomly be populated with when reinitialized.
    Which ones you should actually show are determined by the plug being inserted into the socket, and the socket’s type.
    When you inspect the plug that could go into a Masterwork Socket, look up the socket type of the socket being inspected and find the DestinySocketTypeDefinition.
    Then, look at the Plugs that can fit in that socket. Find the Whitelist in the DestinySocketTypeDefinition that matches the plug item’s categoryhash.
    That whitelist entry will potentially have a new “reinitializationPossiblePlugHashes” property.If it does, that means we know what it will roll if you try to insert this plug into this socket.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
