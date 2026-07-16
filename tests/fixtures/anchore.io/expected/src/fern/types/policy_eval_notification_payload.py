

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .generic_notification_payload import GenericNotificationPayload


class PolicyEvalNotificationPayload(GenericNotificationPayload):
    annotations: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    List of Corresponding Image Annotations
    """

    curr_eval: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The Current Policy Evaluation result
    """

    last_eval: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The Previous Policy Evaluation result
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
