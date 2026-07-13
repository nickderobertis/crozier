

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_email_opt_in_definition import UserEmailOptInDefinition
from .user_email_subscription_definition import UserEmailSubscriptionDefinition
from .user_email_view_definition import UserEmailViewDefinition


class UserEmailSettings(UniversalBaseModel):
    """
    The set of all email subscription/opt-in settings and definitions.
    """

    opt_in_definitions: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, UserEmailOptInDefinition]], FieldMetadata(alias="optInDefinitions")
    ] = pydantic.Field(default=None)
    """
    Keyed by the name identifier of the opt-in definition.
    """

    subscription_definitions: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, UserEmailSubscriptionDefinition]],
        FieldMetadata(alias="subscriptionDefinitions"),
    ] = pydantic.Field(default=None)
    """
    Keyed by the name identifier of the Subscription definition.
    """

    views: typing.Optional[typing.Dict[str, UserEmailViewDefinition]] = pydantic.Field(default=None)
    """
    Keyed by the name identifier of the View definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
