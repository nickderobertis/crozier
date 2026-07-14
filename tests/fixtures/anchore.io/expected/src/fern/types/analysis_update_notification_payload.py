

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .analysis_update_eval import AnalysisUpdateEval
from .generic_notification_payload import GenericNotificationPayload


class AnalysisUpdateNotificationPayload(GenericNotificationPayload):
    annotations: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    List of Corresponding Image Annotations
    """

    curr_eval: typing.Optional[AnalysisUpdateEval] = None
    last_eval: typing.Optional[AnalysisUpdateEval] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
