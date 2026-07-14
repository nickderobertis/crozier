

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .generic_notification_payload import GenericNotificationPayload


class TagUpdateNotificationPayload(GenericNotificationPayload):
    annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    List of Corresponding Image Annotations
    """

    curr_eval: typing.Optional[typing.List[typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    A list containing the current image digest
    """

    last_eval: typing.Optional[typing.List[typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    A list containing the previous image digests
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
