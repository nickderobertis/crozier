

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AliasCollection(UniversalBaseModel):
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
            alias="collectionName", description="The name of the target collection to reassign an alias to."
        ),
    ]
    """
    The name of the target collection to reassign an alias to.
    """

    alias_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="aliasName"),
        pydantic.Field(alias="aliasName", description="The alias of the collection. "),
    ]
    """
    The alias of the collection. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
