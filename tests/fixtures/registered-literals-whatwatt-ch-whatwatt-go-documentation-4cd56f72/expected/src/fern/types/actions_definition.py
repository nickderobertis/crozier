

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .actions_definition_actions_item import ActionsDefinitionActionsItem
from .actions_definition_const_value import ActionsDefinitionConstValue


class ActionsDefinition(UniversalBaseModel):
    const: typing.Optional[typing.Dict[str, ActionsDefinitionConstValue]] = pydantic.Field(default=None)
    """
    Constants for substitution; nulls may be ignored by firmware
    """

    actions: typing.Optional[typing.List[ActionsDefinitionActionsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
