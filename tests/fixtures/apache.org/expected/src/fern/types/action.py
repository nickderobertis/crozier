

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Action(UniversalBaseModel):
    """
    An action Item.

    *New in version 2.1.0*
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the permission "action"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
