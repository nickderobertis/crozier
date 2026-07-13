

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_item_intrinsic_socket_entry_definition import (
    DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition,
)
from .destiny_definitions_destiny_item_socket_category_definition import (
    DestinyDefinitionsDestinyItemSocketCategoryDefinition,
)
from .destiny_definitions_destiny_item_socket_entry_definition import DestinyDefinitionsDestinyItemSocketEntryDefinition


class DestinyDefinitionsDestinyItemSocketBlockDefinition(UniversalBaseModel):
    """
    If defined, the item has at least one socket.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    This was supposed to be a string that would give per-item details about sockets. In practice, it turns out that all this ever has is the localized word "details". ... that's lame, but perhaps it will become something cool in the future.
    """

    intrinsic_sockets: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition]],
        FieldMetadata(alias="intrinsicSockets"),
    ] = pydantic.Field(default=None)
    """
    Each intrinsic (or immutable/permanent) socket on an item is defined here, along with the plug that is permanently affixed to the socket.
    """

    socket_categories: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemSocketCategoryDefinition]],
        FieldMetadata(alias="socketCategories"),
    ] = pydantic.Field(default=None)
    """
    A convenience property, that refers to the sockets in the "sockets" property, pre-grouped by category and ordered in the manner that they should be grouped in the UI. You could form this yourself with the existing data, but why would you want to? Enjoy life man.
    """

    socket_entries: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemSocketEntryDefinition]],
        FieldMetadata(alias="socketEntries"),
    ] = pydantic.Field(default=None)
    """
    Each non-intrinsic (or mutable) socket on an item is defined here. Check inside for more info.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
