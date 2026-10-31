

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_id_int import GroupIdInt
from .node_share_status import NodeShareStatus


class NodeShareState(UniversalBaseModel):
    locked: bool = pydantic.Field()
    """
    True if the node is locked, False otherwise
    """

    current_user_groupids: typing.Optional[typing.List[GroupIdInt]] = pydantic.Field(default=None)
    """
    Group(s) that currently have access to the node (or locked it)
    """

    status: typing.Optional[NodeShareStatus] = pydantic.Field(default=None)
    """
    Reason why the node is locked, None if not locked
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
