

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .variable_name import VariableName


class Database(UniversalBaseModel):
    """
    Represents a collection of schemas.

    Attributes:
        name (str): The name of the database
        dialect (str): The dialect of the database
        schemas (List[Schema]): List of schemas in the database.
        schemas_resolved (bool): True when `schemas` has been enumerated.
            False when schema discovery was deferred. Defaults to True
        engine (Optional[VariableName]): Database engine or connection handler, if any.
    """

    dialect: str
    engine: typing.Optional[VariableName] = None
    name: str
    schemas: typing.List["Schema"]
    schemas_resolved: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .schema import Schema

update_forward_refs(Database, Schema=Schema)
