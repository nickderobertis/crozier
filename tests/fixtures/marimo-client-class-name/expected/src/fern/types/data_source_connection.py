

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .database import Database


class DataSourceConnection(UniversalBaseModel):
    """
    Represents a data source connection.

    Attributes:
        source (str): The source of the data source connection. E.g 'postgres'.
        dialect (str): The dialect of the data source connection. E.g 'postgresql'.
        name (str): The name of the data source connection. E.g 'engine'.
        display_name (str): The display name of the data source connection. E.g 'PostgresQL (engine)'.
        databases (List[Database]): The databases in the data source connection.
        default_database (Optional[str]): The default database in the data source connection.
        default_schema (Optional[str]): The default schema in the data source connection.
    """

    databases: typing.List[Database]
    default_database: typing.Optional[str] = None
    default_schema: typing.Optional[str] = None
    dialect: str
    display_name: str
    name: str
    source: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DataSourceConnection)
