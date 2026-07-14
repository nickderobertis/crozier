

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link_type import LinkType
from .subscriptions_app_pkg_subscription import SubscriptionsAppPkgSubscription


class AppPkgSubscriptionLinkListLinks(UniversalBaseModel):
    """
    Links to resources related to this resource.
    """

    self_: typing_extensions.Annotated[LinkType, FieldMetadata(alias="self")]
    subscriptions: typing.Optional[typing.List[SubscriptionsAppPkgSubscription]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
