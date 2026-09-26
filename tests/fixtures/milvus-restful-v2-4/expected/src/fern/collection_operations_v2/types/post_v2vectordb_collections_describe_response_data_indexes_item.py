

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostV2VectordbCollectionsDescribeResponseDataIndexesItem(UniversalBaseModel):
    field_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fieldName"),
        pydantic.Field(alias="fieldName", description="The target field of this index."),
    ]
    """
    The target field of this index.
    """

    index_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="indexName"), pydantic.Field(alias="indexName", description="The name of this index.")
    ]
    """
    The name of this index.
    """

    metric_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="metricType"),
        pydantic.Field(alias="metricType", description="The metric type of this index."),
    ]
    """
    The metric type of this index.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
