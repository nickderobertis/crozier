

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .data_table import DataTable


class Schema(UniversalBaseModel):
    """
    Represents a database schema and its tables.

    A schema may itself contain nested child schemas, e.g. for catalogs with
    hierarchical namespaces such as Iceberg (`top.nested.deep`).

    Attributes:
        name (str): The name of the schema.
        tables (List[DataTable]): Tables in this schema.
        tables_resolved (bool): True when `tables` has been enumerated
            False when table discovery was deferred. Defaults to True
        child_schemas (List[Schema]): Nested child schemas (sub-namespaces).
        child_schemas_resolved (bool): True when `child_schemas` has been
            enumerated. False when discovery was deferred. Defaults to True
    """

    child_schemas: typing.Optional[typing.List["Schema"]] = None
    child_schemas_resolved: typing.Optional[bool] = None
    name: str
    tables: typing.List[DataTable]
    tables_resolved: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Schema)
