

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemSocketCategoryDefinition(UniversalBaseModel):
    """
    Sockets are grouped into categories in the UI. These define which category and which sockets are under that category.
    """

    socket_category_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="socketCategoryHash"),
        pydantic.Field(
            alias="socketCategoryHash",
            description="The hash for the Socket Category: a quick way to go get the header display information for the category. Use it to look up DestinySocketCategoryDefinition info.",
        ),
    ] = None
    """
    The hash for the Socket Category: a quick way to go get the header display information for the category. Use it to look up DestinySocketCategoryDefinition info.
    """

    socket_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="socketIndexes"),
        pydantic.Field(
            alias="socketIndexes",
            description='Use these indexes to look up the sockets in the "sockets.socketEntries" property on the item definition. These are the indexes under the category, in game-rendered order.',
        ),
    ] = None
    """
    Use these indexes to look up the sockets in the "sockets.socketEntries" property on the item definition. These are the indexes under the category, in game-rendered order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
