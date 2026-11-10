

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_delivery_account import LinkDeliveryAccount
from .link_delivery_institution import LinkDeliveryInstitution
from .link_delivery_webhook_callback_type import LinkDeliveryWebhookCallbackType
from .link_event_name import LinkEventName


class LinkCallbackMetadata(UniversalBaseModel):
    """
    Information related to the callback from the hosted Link session.
    """

    accounts: typing.Optional[typing.List[LinkDeliveryAccount]] = pydantic.Field(default=None)
    """
    A list of accounts attached to the connected Item. If Account Select is enabled via the developer dashboard, accounts will only include selected accounts.
    """

    callback_type: typing.Optional[LinkDeliveryWebhookCallbackType] = None
    event_name: typing.Optional[LinkEventName] = None
    institution: typing.Optional[LinkDeliveryInstitution] = None
    link_session_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier associated with a user's actions and events through the Link flow. Include this identifier when opening a support ticket for faster turnaround.
    """

    request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request ID for the last request made by Link. This can be shared with Plaid Support to expedite investigation.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates where in the flow the Link user exited
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
