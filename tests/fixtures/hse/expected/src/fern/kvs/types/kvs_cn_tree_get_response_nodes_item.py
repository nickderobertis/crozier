

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.cn_statistics import CnStatistics
from .kvs_cn_tree_get_response_nodes_item_kvsets import KvsCnTreeGetResponseNodesItemKvsets


class KvsCnTreeGetResponseNodesItem(CnStatistics):
    """
    Tree node.
    """

    id: typing.Optional[int] = None
    edge_key: typing.Optional[str] = None
    kvsets: typing.Optional[KvsCnTreeGetResponseNodesItemKvsets] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
