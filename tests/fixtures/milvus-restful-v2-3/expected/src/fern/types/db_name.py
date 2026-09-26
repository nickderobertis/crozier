

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DbName(UniversalBaseModel):
    db_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dbName"),
        pydantic.Field(
            alias="dbName",
            description="The name of the database to which the collection belongs.\nSetting this to a non-existing database results in a **MilvusException**.",
        ),
    ] = None
    """
    The name of the database to which the collection belongs.
    Setting this to a non-existing database results in a **MilvusException**.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
