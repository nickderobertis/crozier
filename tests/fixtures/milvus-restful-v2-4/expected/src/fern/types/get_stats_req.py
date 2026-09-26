

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetStatsReq(UniversalBaseModel):
    db_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="dbName"),
        pydantic.Field(
            alias="dbName",
            description="The name of the database which the collection belongs to. Setting this to a non-existing database results in an error.",
        ),
    ]
    """
    The name of the database which the collection belongs to. Setting this to a non-existing database results in an error.
    """

    collection_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="collectionName"),
        pydantic.Field(
            alias="collectionName",
            description="The name of the collection to check.\nSetting this to a non-existing database results in an error.",
        ),
    ]
    """
    The name of the collection to check.
    Setting this to a non-existing database results in an error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
