

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.cn_statistics import CnStatistics
from .kvs_cn_tree_get_response_nodes_item import KvsCnTreeGetResponseNodesItem


class KvsCnTreeGetResponse(CnStatistics):
    kvsets: typing.Optional[int] = None
    nodes: typing.Optional[typing.List[KvsCnTreeGetResponseNodesItem]] = pydantic.Field(default=None)
    """
    List of tree nodes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
