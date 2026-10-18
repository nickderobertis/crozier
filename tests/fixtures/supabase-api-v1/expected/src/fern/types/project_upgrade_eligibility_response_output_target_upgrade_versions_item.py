

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_upgrade_eligibility_response_output_target_upgrade_versions_item_postgres_version import (
    ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion,
)
from .project_upgrade_eligibility_response_output_target_upgrade_versions_item_release_channel import (
    ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel,
)


class ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItem(UniversalBaseModel):
    postgres_version: ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion
    release_channel: ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel
    app_version: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
