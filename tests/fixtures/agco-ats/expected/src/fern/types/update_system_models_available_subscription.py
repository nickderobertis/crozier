

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_available_subscription_subscription_type import (
    UpdateSystemModelsAvailableSubscriptionSubscriptionType,
)
from .update_system_models_package_type import UpdateSystemModelsPackageType


class UpdateSystemModelsAvailableSubscription(UniversalBaseModel):
    package_type: typing_extensions.Annotated[
        typing.Optional[UpdateSystemModelsPackageType],
        FieldMetadata(alias="PackageType"),
        pydantic.Field(alias="PackageType", description="The PackageType this subscription is for."),
    ] = None
    """
    The PackageType this subscription is for.
    """

    subscription_type: typing_extensions.Annotated[
        typing.Optional[UpdateSystemModelsAvailableSubscriptionSubscriptionType],
        FieldMetadata(alias="SubscriptionType"),
        pydantic.Field(alias="SubscriptionType", description="The type of subscription supported."),
    ] = None
    """
    The type of subscription supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
