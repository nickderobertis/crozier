

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .migration_config_policies_dto import MigrationConfigPoliciesDto


class MigrationConfigDto(UniversalBaseModel):
    policies: MigrationConfigPoliciesDto
    vcs: typing.List[str]
    vps: typing.List[str]
    schemas: typing.Dict[str, typing.Any]
    groups: typing.Dict[str, typing.Any]
    roles: typing.Dict[str, typing.Any]
    blocks: typing.Dict[str, typing.Any]
    tokens: typing.Dict[str, typing.Any]
    migrate_state: typing_extensions.Annotated[
        bool, FieldMetadata(alias="migrateState"), pydantic.Field(alias="migrateState")
    ]
    migrate_retire_pools: typing_extensions.Annotated[
        bool, FieldMetadata(alias="migrateRetirePools"), pydantic.Field(alias="migrateRetirePools")
    ]
    edited_v_cs: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="editedVCs"), pydantic.Field(alias="editedVCs")
    ]
    retire_contract_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="retireContractId"), pydantic.Field(alias="retireContractId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
