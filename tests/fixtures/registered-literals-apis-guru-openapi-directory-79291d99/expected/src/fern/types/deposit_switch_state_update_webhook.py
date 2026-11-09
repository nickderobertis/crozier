

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_environment_values import WebhookEnvironmentValues


class DepositSwitchStateUpdateWebhook(UniversalBaseModel):
    """
    Fired when the status of a deposit switch request has changed.
    """

    deposit_switch_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the deposit switch.
    """

    environment: typing.Optional[WebhookEnvironmentValues] = None
    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    The state, or status, of the deposit switch.
    
    `initialized`: The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.
    
    `processing`: The deposit switch request has been submitted and is being processed.
    
    `completed`: The user's employer has fulfilled and completed the deposit switch request.
    
    `error`: There was an error processing the deposit switch request.
    
    For more information, see the [Deposit Switch API reference](/docs/deposit-switch/reference#deposit_switchget).
    """

    webhook_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    `"SWITCH_STATE_UPDATE"`
    """

    webhook_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    `"DEPOSIT_SWITCH"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
