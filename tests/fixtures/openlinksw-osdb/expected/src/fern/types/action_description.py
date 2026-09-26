

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_point import EntryPoint


class ActionDescription(UniversalBaseModel):
    action_id: str = pydantic.Field()
    """
    A unique one word identifier for the action.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A short description of the action.
    """

    entry_point: EntryPoint

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
