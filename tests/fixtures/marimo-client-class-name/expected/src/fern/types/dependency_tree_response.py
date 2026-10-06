

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class DependencyTreeResponse(UniversalBaseModel):
    tree: typing.Optional["DependencyTreeNode"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .dependency_tree_node import DependencyTreeNode

update_forward_refs(DependencyTreeResponse, DependencyTreeNode=DependencyTreeNode)
