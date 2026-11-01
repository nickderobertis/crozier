

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .condition import Condition


class NodePoolConditions(UniversalBaseModel):
    """
    Lifecycle conditions of a node pool. Each is a Condition.
    """

    provisioning: Condition = pydantic.Field()
    """
    The node pool is provisioning.
    """

    provisioned: Condition = pydantic.Field()
    """
    The node pool is provisioned.
    """

    deleting: Condition = pydantic.Field()
    """
    The node pool is being deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
