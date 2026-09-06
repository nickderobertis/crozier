

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_system_models_package_type_i_dto_bundle_subscription_type import (
    UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType,
)


class UpdateSystemModelsPackageTypeIDtoBundle(UniversalBaseModel):
    bundle_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="BundleID"),
        pydantic.Field(alias="BundleID", description="The bundle to include the package in."),
    ]
    """
    The bundle to include the package in.
    """

    package_type_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="PackageTypeID"),
        pydantic.Field(alias="PackageTypeID", description="The package type id of the package to include"),
    ]
    """
    The package type id of the package to include
    """

    package_version: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="PackageVersion"),
        pydantic.Field(alias="PackageVersion", description="The package version of the package to include"),
    ]
    """
    The package version of the package to include
    """

    priority: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Priority"),
        pydantic.Field(
            alias="Priority",
            description="The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.",
        ),
    ]
    """
    The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.
    """

    subscription_type: typing_extensions.Annotated[
        typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType],
        FieldMetadata(alias="SubscriptionType"),
        pydantic.Field(
            alias="SubscriptionType",
            description="Optional. The type of subscription supported.  The default subscription type is Required.",
        ),
    ] = None
    """
    Optional. The type of subscription supported.  The default subscription type is Required.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
