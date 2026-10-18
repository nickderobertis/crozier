

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_upgrade_eligibility_response_output_current_app_version_release_channel import (
    ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel,
)
from .project_upgrade_eligibility_response_output_target_upgrade_versions_item import (
    ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItem,
)
from .project_upgrade_eligibility_response_output_validation_errors_item import (
    ProjectUpgradeEligibilityResponseOutputValidationErrorsItem,
)
from .project_upgrade_eligibility_response_output_warnings_item import (
    ProjectUpgradeEligibilityResponseOutputWarningsItem,
)


class ProjectUpgradeEligibilityResponseOutput(UniversalBaseModel):
    eligible: bool
    current_app_version: str
    current_app_version_release_channel: ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel
    latest_app_version: str
    target_upgrade_versions: typing.List[ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItem]
    duration_estimate_hours: float
    legacy_auth_custom_roles: typing.List[str]
    objects_to_be_dropped: typing.List[str] = pydantic.Field()
    """
    Use validation_errors instead.
    """

    unsupported_extensions: typing.List[str] = pydantic.Field()
    """
    Use validation_errors instead.
    """

    user_defined_objects_in_internal_schemas: typing.List[str] = pydantic.Field()
    """
    Use validation_errors instead.
    """

    validation_errors: typing.List[ProjectUpgradeEligibilityResponseOutputValidationErrorsItem]
    warnings: typing.List[ProjectUpgradeEligibilityResponseOutputWarningsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
