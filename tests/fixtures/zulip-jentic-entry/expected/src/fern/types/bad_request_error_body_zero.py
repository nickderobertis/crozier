

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bad_request_error_body_zero_errors_item_item import BadRequestErrorBodyZeroErrorsItemItem


class BadRequestErrorBodyZero(UniversalBaseModel):
    """
    An example JSON error response for when some of the specified email addresses
    have existing Zulip accounts.
    """

    result: typing.Any
    msg: typing.Any
    code: typing.Any
    errors: typing.Optional[typing.List[typing.List[BadRequestErrorBodyZeroErrorsItemItem]]] = pydantic.Field(
        default=None
    )
    """
    An array of arrays of length 3, where each inner array consists of (a) an email
    address that was skipped while sending invitations, (b) the corresponding error
    message, and (c) a boolean which is `true` when the email address already uses Zulip
    and the corresponding user is deactivated in the organization.
    """

    sent_invitations: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether any invitations were sent.
    """

    daily_limit_reached: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the limit on the number of invitations that can
    be sent in the organization in a day has been reached.
    """

    license_limit_reached: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean specifying whether the organization have enough unused Zulip licenses
    to invite specified number of users.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
