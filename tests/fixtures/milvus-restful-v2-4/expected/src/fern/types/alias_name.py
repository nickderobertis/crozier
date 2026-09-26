

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AliasName(UniversalBaseModel):
    db_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dbName"),
        pydantic.Field(alias="dbName", description="The name of the database to which the collection belongs."),
    ] = None
    """
    The name of the database to which the collection belongs.
    """

    collection_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="collectionName"),
        pydantic.Field(
            alias="collectionName", description="The name of the collection to which the alias is assigned to."
        ),
    ]
    """
    The name of the collection to which the alias is assigned to.
    """

    alias_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="aliasName"),
        pydantic.Field(
            alias="aliasName",
            description="The alias to drop.\nWhen dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.",
        ),
    ]
    """
    The alias to drop.
    When dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
