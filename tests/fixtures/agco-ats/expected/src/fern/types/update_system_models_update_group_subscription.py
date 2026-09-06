

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsUpdateGroupSubscription(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="ClientID"), pydantic.Field(alias="ClientID", description="The ClientID.")
    ]
    """
    The ClientID.
    """

    include: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="Include"),
        pydantic.Field(alias="Include", description="True to receive content of type indicated by PackageTypeID."),
    ]
    """
    True to receive content of type indicated by PackageTypeID.
    """

    package_type_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="PackageTypeID"),
        pydantic.Field(alias="PackageTypeID", description="The PackageType to set subscription status for"),
    ]
    """
    The PackageType to set subscription status for
    """

    update_group_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="UpdateGroupID"),
        pydantic.Field(alias="UpdateGroupID", description="The Update Group this subscription is relevant for."),
    ]
    """
    The Update Group this subscription is relevant for.
    """

    update_group_subscription_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="UpdateGroupSubscriptionID"),
        pydantic.Field(
            alias="UpdateGroupSubscriptionID",
            description="The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.",
        ),
    ] = None
    """
    The Update Group Subscription ID.  This ID will be automatically assigned when creating an Update Group Subscription.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
