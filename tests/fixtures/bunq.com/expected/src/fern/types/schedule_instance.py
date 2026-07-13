

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error import Error
from .request_inquiry_reference import RequestInquiryReference
from .schedule_anchor_object import ScheduleAnchorObject
from .schedule_instance_anchor_object import ScheduleInstanceAnchorObject


class ScheduleInstance(UniversalBaseModel):
    error_message: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The message when the scheduled instance has run and failed due to user error.
    """

    request_reference_split_the_bill: typing.Optional[typing.List[RequestInquiryReference]] = pydantic.Field(
        default=None
    )
    """
    The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    """

    result_object: typing.Optional[ScheduleInstanceAnchorObject] = pydantic.Field(default=None)
    """
    The result object of this schedule instance. (Payment, PaymentBatch)
    """

    scheduled_object: typing.Optional[ScheduleAnchorObject] = pydantic.Field(default=None)
    """
    The scheduled object. (Payment, PaymentBatch)
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state of the scheduleInstance. (FINISHED_SUCCESSFULLY, RETRY, FAILED_USER_ERROR)
    """

    time_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The schedule end time (UTC).
    """

    time_start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The schedule start time (UTC).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ScheduleInstance)
