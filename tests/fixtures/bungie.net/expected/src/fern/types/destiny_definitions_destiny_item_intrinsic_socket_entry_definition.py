

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition(UniversalBaseModel):
    """
    Represents a socket that has a plug associated with it intrinsically. This is useful for situations where the weapon needs to have a visual plug/Mod on it, but that plug/Mod should never change.
    """

    default_visible: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="defaultVisible"),
        pydantic.Field(
            alias="defaultVisible",
            description="If true, then this socket is visible in the item's \"default\" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.",
        ),
    ] = None
    """
    If true, then this socket is visible in the item's "default" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.
    """

    plug_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plugItemHash"),
        pydantic.Field(
            alias="plugItemHash", description="Indicates the plug that is intrinsically inserted into this socket."
        ),
    ] = None
    """
    Indicates the plug that is intrinsically inserted into this socket.
    """

    socket_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="socketTypeHash"),
        pydantic.Field(alias="socketTypeHash", description="Indicates the type of this intrinsic socket."),
    ] = None
    """
    Indicates the type of this intrinsic socket.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
