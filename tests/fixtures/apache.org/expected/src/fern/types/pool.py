

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Pool(UniversalBaseModel):
    """
    The pool
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the pool.
    
    *New in version 2.3.0*
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of pool.
    """

    occupied_slots: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of slots used by running/queued tasks at the moment.
    """

    open_slots: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of free slots at the moment.
    """

    queued_slots: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of slots used by queued tasks at the moment.
    """

    slots: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of slots that can be assigned to tasks. One job may occupy one or more slots.
    """

    used_slots: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of slots used by running tasks at the moment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
