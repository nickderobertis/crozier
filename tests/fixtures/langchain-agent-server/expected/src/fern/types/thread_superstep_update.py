

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .command import Command
from .thread_superstep_update_values import ThreadSuperstepUpdateValues


class ThreadSuperstepUpdate(UniversalBaseModel):
    values: typing.Optional[ThreadSuperstepUpdateValues] = None
    command: typing.Optional[Command] = pydantic.Field(default=None)
    """
    The command associated with the update.
    """

    as_node: str = pydantic.Field()
    """
    Update the state as if this node had just executed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
