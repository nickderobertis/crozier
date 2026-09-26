

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .index_param_index_config import IndexParamIndexConfig


class IndexParam(UniversalBaseModel):
    metric_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="metricType"),
        pydantic.Field(
            alias="metricType",
            description="The similarity metric type used to build the index.\nPossible values for float vector embeddings.\n- For an Milvus instance, possible values are **L2**, **IP**, and **COSINE**, and those for binary vector embeddings are **Jaccard** and **Hamming**.  For details, refer to [Similarity Metrics](https://milvus.io/docs/metric.md).\n- For a Zilliz Cloud cluster, possible values are **L2**, **IP**, and **COSINE**. Read [Similarity Metrics Explained](https://docs.zilliz.com/docs/search-metrics-explained) to get more.",
        ),
    ]
    """
    The similarity metric type used to build the index.
    Possible values for float vector embeddings.
    - For an Milvus instance, possible values are **L2**, **IP**, and **COSINE**, and those for binary vector embeddings are **Jaccard** and **Hamming**.  For details, refer to [Similarity Metrics](https://milvus.io/docs/metric.md).
    - For a Zilliz Cloud cluster, possible values are **L2**, **IP**, and **COSINE**. Read [Similarity Metrics Explained](https://docs.zilliz.com/docs/search-metrics-explained) to get more.
    """

    field_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fieldName"),
        pydantic.Field(
            alias="fieldName", description="The name of the target field on which an index is to be created."
        ),
    ]
    """
    The name of the target field on which an index is to be created.
    """

    index_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="indexName"),
        pydantic.Field(
            alias="indexName",
            description="The name of the index to create, the value defaults to the target field name.",
        ),
    ]
    """
    The name of the index to create, the value defaults to the target field name.
    """

    index_config: typing_extensions.Annotated[
        typing.Optional[IndexParamIndexConfig],
        FieldMetadata(alias="indexConfig"),
        pydantic.Field(
            alias="indexConfig",
            description="The index type and related settings. For details, refer to [Vector Indexes](https://milvus.io/docs/index.md).",
        ),
    ] = None
    """
    The index type and related settings. For details, refer to [Vector Indexes](https://milvus.io/docs/index.md).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
