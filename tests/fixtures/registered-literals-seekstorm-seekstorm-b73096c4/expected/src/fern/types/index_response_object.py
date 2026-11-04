

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .min_max_field_json import MinMaxFieldJson
from .schema_field import SchemaField


class IndexResponseObject(UniversalBaseModel):
    """
    Index response object
    """

    id: int = pydantic.Field()
    """
    Index ID
    """

    name: str = pydantic.Field()
    """
    Index name
    """

    schema_: typing_extensions.Annotated[
        typing.Dict[str, SchemaField],
        FieldMetadata(alias="schema"),
        pydantic.Field(alias="schema", description="Schema definition for the index"),
    ]
    """
    Schema definition for the index
    """

    indexed_doc_count: int = pydantic.Field()
    """
    Number of indexed documents
    """

    committed_doc_count: int = pydantic.Field()
    """
    Number of committed documents
    """

    operations_count: int = pydantic.Field()
    """
    Number of operations: index, update, delete, queries
    """

    query_count: int = pydantic.Field()
    """
    Number of queries, for quotas and billing
    """

    version: str = pydantic.Field()
    """
    SeekStorm version the index was created with
    """

    facets_minmax: typing.Dict[str, MinMaxFieldJson] = pydantic.Field()
    """
    Minimum and maximum values of numeric facet fields
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
