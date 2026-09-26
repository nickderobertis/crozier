

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.cn_statistics import CnStatistics
from .kvs_cn_tree_get_response_nodes_item_kvsets_one_item_job import KvsCnTreeGetResponseNodesItemKvsetsOneItemJob


class KvsCnTreeGetResponseNodesItemKvsetsOneItem(CnStatistics):
    """
    Kvset.
    """

    compc: typing.Optional[int] = None
    vgroups: typing.Optional[int] = None
    rule: typing.Optional[str] = None
    job: typing.Optional[KvsCnTreeGetResponseNodesItemKvsetsOneItemJob] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
