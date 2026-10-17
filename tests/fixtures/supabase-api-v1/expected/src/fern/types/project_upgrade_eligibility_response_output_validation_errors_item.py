

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_upgrade_eligibility_response_output_validation_errors_item_user_defined_objects_in_internal_schemas_obj_type import (
    ProjectUpgradeEligibilityResponseOutputValidationErrorsItemUserDefinedObjectsInInternalSchemasObjType,
)


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_ObjectsDependingOnPgCron(UniversalBaseModel):
    type: typing.Literal["objects_depending_on_pg_cron"] = "objects_depending_on_pg_cron"
    dependents: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_IndexesReferencingLlToEarth(UniversalBaseModel):
    type: typing.Literal["indexes_referencing_ll_to_earth"] = "indexes_referencing_ll_to_earth"
    schema_name: str
    table_name: str
    index_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_FunctionUsingObsoleteLang(UniversalBaseModel):
    type: typing.Literal["function_using_obsolete_lang"] = "function_using_obsolete_lang"
    schema_name: str
    function_name: str
    lang_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UnsupportedExtension(UniversalBaseModel):
    type: typing.Literal["unsupported_extension"] = "unsupported_extension"
    extension_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UnsupportedFdwHandler(UniversalBaseModel):
    type: typing.Literal["unsupported_fdw_handler"] = "unsupported_fdw_handler"
    fdw_name: str
    fdw_handler_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UnloggedTableWithPersistentSequence(
    UniversalBaseModel
):
    type: typing.Literal["unlogged_table_with_persistent_sequence"] = "unlogged_table_with_persistent_sequence"
    schema_name: str
    table_name: str
    sequence_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UserDefinedObjectsInInternalSchemas(
    UniversalBaseModel
):
    type: typing.Literal["user_defined_objects_in_internal_schemas"] = "user_defined_objects_in_internal_schemas"
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


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_ActiveReplicationSlot(UniversalBaseModel):
    type: typing.Literal["active_replication_slot"] = "active_replication_slot"
    slot_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_X86Architecture(UniversalBaseModel):
    type: typing.Literal["x86_architecture"] = "x86_architecture"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_ProjectHibernating(UniversalBaseModel):
    type: typing.Literal["project_hibernating"] = "project_hibernating"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ProjectUpgradeEligibilityResponseOutputValidationErrorsItem = typing_extensions.Annotated[
    typing.Union[
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_ObjectsDependingOnPgCron,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_IndexesReferencingLlToEarth,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_FunctionUsingObsoleteLang,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UnsupportedExtension,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UnsupportedFdwHandler,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UnloggedTableWithPersistentSequence,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_UserDefinedObjectsInInternalSchemas,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_ActiveReplicationSlot,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_X86Architecture,
        ProjectUpgradeEligibilityResponseOutputValidationErrorsItem_ProjectHibernating,
    ],
    pydantic.Field(discriminator="type"),
]
