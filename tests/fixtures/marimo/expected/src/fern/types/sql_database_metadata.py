

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SqlDatabaseMetadata(UniversalBaseModel):
    """
    SQL database metadata.

        Attributes:
            connection: Connection identifier.
            database: Database name.
            schema_path: Parent schema path the schemas belong under. Empty for
                the database's top level.
    """

    connection: str
    database: str
    schema_path: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
