

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .department_tree_node_node import DepartmentTreeNodeNode


class DepartmentTreeNode(UniversalBaseModel):
    node: typing.Optional[DepartmentTreeNodeNode] = None
    children: typing.Optional[typing.List["DepartmentTreeNode"]] = pydantic.Field(default=None)
    """
    List of all children departments.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(DepartmentTreeNode)
