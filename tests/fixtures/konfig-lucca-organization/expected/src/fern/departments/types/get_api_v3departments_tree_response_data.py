

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class GetApiV3DepartmentsTreeResponseData(UniversalBaseModel):
    node: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Root department. Always null.
    """

    children: typing.Optional[typing.List["DepartmentTreeNode"]] = pydantic.Field(default=None)
    """
    Max depth: 9 levels
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from ...types.department_tree_node import DepartmentTreeNode

update_forward_refs(GetApiV3DepartmentsTreeResponseData, DepartmentTreeNode=DepartmentTreeNode)
