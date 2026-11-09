

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class UserPermissionRevokedWebhook(UniversalBaseModel):
    """
    The `USER_PERMISSION_REVOKED` webhook is fired when an end user has used either the [my.plaid.com portal](https://my.plaid.com) or the financial institution’s consent portal to revoke the permission that they previously granted to access an Item. Once access to an Item has been revoked, it cannot be restored. If the user subsequently returns to your application, a new Item must be created for the user.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `USER_PERMISSION_REVOKED`
    """

    webhook_type: str = pydantic.Field()
    """
    `ITEM`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
