

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_available_subscription import UpdateSystemModelsAvailableSubscription
from .update_system_models_update_group import UpdateSystemModelsUpdateGroup


class UpdateSystemModelsAvailableUpdateGroupSubscription(UniversalBaseModel):
    available_subscriptions: typing_extensions.Annotated[
        typing.Optional[typing.List[UpdateSystemModelsAvailableSubscription]],
        FieldMetadata(alias="AvailableSubscriptions"),
        pydantic.Field(
            alias="AvailableSubscriptions", description="The available subscriptions for this update group."
        ),
    ] = None
    """
    The available subscriptions for this update group.
    """

    update_group: typing_extensions.Annotated[
        typing.Optional[UpdateSystemModelsUpdateGroup],
        FieldMetadata(alias="UpdateGroup"),
        pydantic.Field(alias="UpdateGroup", description="The Update Group this subscription is for."),
    ] = None
    """
    The Update Group this subscription is for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
