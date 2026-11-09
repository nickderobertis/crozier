

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .wizard_api_set_policy_async_request_wizard_config_schemas_item_roles_config_item_grid_columns_item import (
    WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItemGridColumnsItem,
)


class WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItem(UniversalBaseModel):
    role: typing.Optional[str] = None
    is_approver: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isApprover"), pydantic.Field(alias="isApprover")
    ] = None
    is_creator: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCreator"), pydantic.Field(alias="isCreator")
    ] = None
    grid_columns: typing_extensions.Annotated[
        typing.Optional[
            typing.List[WizardApiSetPolicyAsyncRequestWizardConfigSchemasItemRolesConfigItemGridColumnsItem]
        ],
        FieldMetadata(alias="gridColumns"),
        pydantic.Field(alias="gridColumns"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
