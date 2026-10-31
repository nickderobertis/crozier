

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .node_taint_effect import NodeTaintEffect


class NodeTaint(UniversalBaseModel):
    """
    A Kubernetes taint applied to nodes in a pool.
    """

    key: str = pydantic.Field()
    """
    Taint key.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Taint value. Empty is valid.
    """

    effect: NodeTaintEffect

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
