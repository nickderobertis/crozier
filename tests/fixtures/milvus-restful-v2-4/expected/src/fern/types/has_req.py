

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HasReq(UniversalBaseModel):
    db_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="dbName"),
        pydantic.Field(
            alias="dbName", description="The name of the database in which to check the existence of a collection."
        ),
    ]
    """
    The name of the database in which to check the existence of a collection.
    """

    collection_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="collectionName"),
        pydantic.Field(alias="collectionName", description="The name of an existing collection."),
    ]
    """
    The name of an existing collection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
