

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .liabilities_account_ids_with_updated_liabilities import LiabilitiesAccountIdsWithUpdatedLiabilities
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class LiabilitiesDefaultUpdateWebhook(UniversalBaseModel):
    """
    The webhook of type `LIABILITIES` and code `DEFAULT_UPDATE` will be fired when new or updated liabilities have been detected on a liabilities item.
    """

    account_ids_with_new_liabilities: typing.List[str] = pydantic.Field()
    """
    An array of `account_id`'s for accounts that contain new liabilities.'
    """

    account_ids_with_updated_liabilities: LiabilitiesAccountIdsWithUpdatedLiabilities
    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `DEFAULT_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `LIABILITIES`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
