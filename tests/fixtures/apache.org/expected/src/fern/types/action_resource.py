

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action import Action
from .resource import Resource


class ActionResource(UniversalBaseModel):
    """
    The Action-Resource item.

    *New in version 2.1.0*
    """

    action: typing.Optional[Action] = pydantic.Field(default=None)
    """
    The permission action
    """

    resource: typing.Optional[Resource] = pydantic.Field(default=None)
    """
    The permission resource
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
