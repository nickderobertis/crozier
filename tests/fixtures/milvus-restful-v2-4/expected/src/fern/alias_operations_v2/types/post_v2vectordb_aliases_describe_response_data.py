

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostV2VectordbAliasesDescribeResponseData(UniversalBaseModel):
    db_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="dbName"),
        pydantic.Field(alias="dbName", description="The name of the database to which the collection belongs."),
    ]
    """
    The name of the database to which the collection belongs.
    """

    collection_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="collectionName"),
        pydantic.Field(alias="collectionName", description="the name of the collection to which an alias belongs."),
    ]
    """
    the name of the collection to which an alias belongs.
    """

    alias_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="aliasName"), pydantic.Field(alias="aliasName", description="The name of the alias.")
    ]
    """
    The name of the alias.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
