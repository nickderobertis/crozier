

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition(UniversalBaseModel):
    """
    The definition of a known, reusable plug that can be applied to a socket.
    """

    plug_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="plugItemHash"),
        pydantic.Field(
            alias="plugItemHash",
            description="The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.",
        ),
    ] = None
    """
    The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
