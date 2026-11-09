

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_profile_status import PaymentProfileStatus
from .request_id import RequestId


class PaymentProfileGetResponse(UniversalBaseModel):
    """
    PaymentProfileGetResponse defines the response schema for `/payment_profile/get`
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the time the given Payment Profile was created at
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the time the given Payment Profile was deleted at. Always `null` if the Payment Profile has not been deleted
    """

    request_id: RequestId
    status: PaymentProfileStatus
    updated_at: dt.datetime = pydantic.Field()
    """
    Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:mm:ssZ`) indicating the last time the given Payment Profile was updated at
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
