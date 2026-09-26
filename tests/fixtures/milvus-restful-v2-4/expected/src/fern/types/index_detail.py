

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IndexDetail(UniversalBaseModel):
    field_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fieldName"),
        pydantic.Field(alias="fieldName", description="The name of the target field."),
    ]
    """
    The name of the target field.
    """

    index_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="indexName"), pydantic.Field(alias="indexName", description="The name of the index.")
    ]
    """
    The name of the index.
    """

    index_state: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="indexState"),
        pydantic.Field(alias="indexState", description="The status of the indexing progress."),
    ]
    """
    The status of the indexing progress.
    """

    index_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="indexType"), pydantic.Field(alias="indexType", description="The type of this index.")
    ]
    """
    The type of this index.
    """

    indexed_rows: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="indexedRows"),
        pydantic.Field(alias="indexedRows", description="The total number o rows that have been indexed."),
    ]
    """
    The total number o rows that have been indexed.
    """

    metric_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="metricType"),
        pydantic.Field(alias="metricType", description="The type of the metric."),
    ]
    """
    The type of the metric.
    """

    pending_rows: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pendingRows"),
        pydantic.Field(alias="pendingRows", description="The number of rows that are waiting to be indexed."),
    ]
    """
    The number of rows that are waiting to be indexed.
    """

    total_rows: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalRows"),
        pydantic.Field(alias="totalRows", description="The total number of entities/rows"),
    ]
    """
    The total number of entities/rows
    """

    fail_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="failReason"),
        pydantic.Field(alias="failReason", description="The reason for the failure to build indexes."),
    ] = None
    """
    The reason for the failure to build indexes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
