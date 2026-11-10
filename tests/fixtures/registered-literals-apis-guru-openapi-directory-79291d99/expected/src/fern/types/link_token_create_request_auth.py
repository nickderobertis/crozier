

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_token_create_request_auth_flow_type import LinkTokenCreateRequestAuthFlowType


class LinkTokenCreateRequestAuth(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with the Auth product. This field can be used to enable or disable extended Auth flows for the resulting Link session. Omitting any field will result in a default that can be configured by your account manager.
    """

    auth_type_select_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether Auth Type Select is enabled for the Link session, allowing the end user to choose between linking instantly or manually prior to selecting their financial institution. Note that this can only be true if `same_day_microdeposits_enabled` is set to true.
    """

    automated_microdeposits_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether the Link session is enabled for the Automated Micro-deposits flow.
    """

    flow_type: typing.Optional[LinkTokenCreateRequestAuthFlowType] = pydantic.Field(default=None)
    """
    This field has been deprecated in favor of `auth_type_select_enabled`.
    """

    instant_match_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether the Link session is enabled for the Instant Match flow. As of November 2022, Instant Match will be enabled by default. Instant Match can be disabled by setting this field to `false`.
    """

    same_day_microdeposits_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Specifies whether the Link session is enabled for the Same Day Micro-deposits flow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
