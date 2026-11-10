

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_end_customer_o_auth_status_updated_values import PartnerEndCustomerOAuthStatusUpdatedValues
from .webhook_environment_values import WebhookEnvironmentValues


class PartnerEndCustomerOAuthStatusUpdatedWebhook(UniversalBaseModel):
    """
    The webhook of type `PARTNER` and code `END_CUSTOMER_OAUTH_STATUS_UPDATED` will be fired when a partner's end customer has an update on their OAuth registration status with an institution.
    """

    end_customer_client_id: str = pydantic.Field()
    """
    The client ID of the end customer
    """

    environment: WebhookEnvironmentValues
    institution_id: str = pydantic.Field()
    """
    The institution ID
    """

    institution_name: str = pydantic.Field()
    """
    The institution name
    """

    status: PartnerEndCustomerOAuthStatusUpdatedValues
    webhook_code: str = pydantic.Field()
    """
    `END_CUSTOMER_OAUTH_STATUS_UPDATED`
    """

    webhook_type: str = pydantic.Field()
    """
    `PARTNER`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
