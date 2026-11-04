

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_actions_response_actions_item import SetActionsResponseActionsItem
from .set_actions_response_const_value import SetActionsResponseConstValue


class SetActionsResponse(UniversalBaseModel):
    const: typing.Optional[typing.Dict[str, SetActionsResponseConstValue]] = pydantic.Field(default=None)
    """
    Constants for substitution; nulls may be ignored by firmware
    """

    actions: typing.Optional[typing.List[SetActionsResponseActionsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
