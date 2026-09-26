

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV2VectordbEntitiesSearchRequestSearchParams(UniversalBaseModel):
    """
     The parameter settings specific to this operation.
    - **metric_type** (*str*) -
      -   The metric type applied to this operation. This should be the same as the one used when you index the vector field specified above.
      -   Possible values are **L2**, **IP**, and **COSINE**.
    - **params** (dict) -
      -   Additional parameters
      - **radius** (float) -
        -    Determines the threshold of least similarity. When setting `metric_type` to `L2`, ensure that this value is greater than that of **range_filter**. Otherwise, this value should be lower than that of **range_filter**.
      - **range_filter**  (float) -
        -    Refines the search to vectors within a specific similarity range. When setting `metric_type` to `IP` or `COSINE`, ensure that this value is greater than that of **radius**. Otherwise, this value should be lower than that of **radius**.
    <include target="milvus">
    For details on other applicable search parameters, refer to [In-memory Index](https://milvus.io/docs/index.md) and [On-disk Index](https://milvus.io/docs/disk_index.md).
    </include>
    <include target="zilliz">
    For details on other applicable search parameters, read [AUTOINDEX Explained](https://docs.zilliz.com/docs/autoindex-explained) to get more.
    </include>
    """

    radius: typing.Optional[int] = pydantic.Field(default=None)
    """
          Determines the threshold of least similarity. When setting metric_type to L2, ensure that this value is greater than that of range_filter. Otherwise, this value should be lower than that of range_filter. 
    """

    range_filter: typing.Optional[int] = pydantic.Field(default=None)
    """
          Refines the search to vectors within a specific similarity range. When setting metric_type to IP or COSINE, ensure that this value is greater than that of radius. Otherwise, this value should be lower than that of radius. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
