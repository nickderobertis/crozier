

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_response_account_deletion import MeResponseAccountDeletion
from .me_subscription import MeSubscription


class MeResponseAccount(UniversalBaseModel):
    """
    Account state for the current user
    """

    deletion: MeResponseAccountDeletion = pydantic.Field()
    """
    Provider state relevant to account deletion
    """

    has_active_subscription: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasActiveSubscription"),
        pydantic.Field(
            alias="hasActiveSubscription", description="Whether the account has an active or trialing subscription"
        ),
    ]
    """
    Whether the account has an active or trialing subscription
    """

    subscription: typing.Optional[MeSubscription] = pydantic.Field(default=None)
    """
    Active subscription details, when present
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
