

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_upgrade_eligibility_response_output_validation_errors_item_user_defined_objects_in_internal_schemas_obj_type import (
    ProjectUpgradeEligibilityResponseOutputValidationErrorsItemUserDefinedObjectsInInternalSchemasObjType,
)


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItemUserDefinedObjectsInInternalSchemas(
    UniversalBaseModel
):
    obj_type: ProjectUpgradeEligibilityResponseOutputValidationErrorsItemUserDefinedObjectsInInternalSchemasObjType
    schema_name: str
    obj_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
