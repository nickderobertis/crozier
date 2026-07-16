

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .href import Href
from .subsctiption_type_app_pkg import SubsctiptionTypeAppPkg


class SubscriptionsAppPkgSubscription(UniversalBaseModel):
    """
    'The data type represents the input parameters of "subscription operation" to notification of application package management for the onboarding, or operational state change of application package.'
    """

    href: Href
    subsctiption_type: typing_extensions.Annotated[
        SubsctiptionTypeAppPkg, FieldMetadata(alias="subsctiptionType"), pydantic.Field(alias="subsctiptionType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
