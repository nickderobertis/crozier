

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class NbBatchImportTree(UniversalBaseModel):
    parent: int
    tree: typing.List["ImportNode"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .import_node import ImportNode
from .import_node_children import ImportNodeChildren

update_forward_refs(NbBatchImportTree, ImportNode=ImportNode, ImportNodeChildren=ImportNodeChildren)
