

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_pkg_subscription_link_list_links import AppPkgSubscriptionLinkListLinks


class AppPkgSubscriptionLinkList(UniversalBaseModel):
    """
    'The data type represents a subscription link list of notification on application package management'
    """

    links: typing_extensions.Annotated[AppPkgSubscriptionLinkListLinks, FieldMetadata(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
