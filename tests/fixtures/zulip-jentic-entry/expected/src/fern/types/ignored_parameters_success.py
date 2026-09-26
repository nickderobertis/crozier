

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IgnoredParametersSuccess(UniversalBaseModel):
    """
    **Changes**: The [`ignored_parameters_unsupported`][ignored_params]
    array was added as a possible return value for all REST API endpoint
    JSON success responses in Zulip 7.0 (feature level 167).

    Previously, it was added to
    [`POST /users/me/subscriptions/properties`](/api/update-subscription-settings)
    in Zulip 5.0 (feature level 111) and to
    [`PATCH /realm/user_settings_defaults`](/api/update-realm-user-settings-defaults)
    in Zulip 5.0 (feature level 96). The feature was introduced in Zulip 5.0
    (feature level 78) as a return value for the
    [`PATCH /settings`](/api/update-settings) endpoint.

    A typical successful JSON response with ignored parameters may look like:

    [ignored_params]: /api/rest-error-handling#ignored-parameters
    """

    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
