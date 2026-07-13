

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_email_subscription_definition import UserEmailSubscriptionDefinition


class UserEmailOptInDefinition(UniversalBaseModel):
    """
    Defines a single opt-in category: a wide-scoped permission to send emails for the subject related to the opt-in.
    """

    dependent_subscriptions: typing_extensions.Annotated[
        typing.Optional[typing.List[UserEmailSubscriptionDefinition]], FieldMetadata(alias="dependentSubscriptions")
    ] = pydantic.Field(default=None)
    """
    Information about the dependent subscriptions for this opt-in.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for this opt-in category.
    """

    set_by_default: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="setByDefault")] = (
        pydantic.Field(default=None)
    )
    """
    If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they're opting into.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    The flag value for this opt-in category. For historical reasons, this is defined as a flags enum.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
