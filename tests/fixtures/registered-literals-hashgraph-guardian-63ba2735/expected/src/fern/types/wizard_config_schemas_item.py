

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .wizard_config_schemas_item_mint_options import WizardConfigSchemasItemMintOptions
from .wizard_config_schemas_item_roles_config_item import WizardConfigSchemasItemRolesConfigItem


class WizardConfigSchemasItem(UniversalBaseModel):
    name: typing.Optional[str] = None
    iri: typing.Optional[str] = None
    is_approve_enable: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isApproveEnable"), pydantic.Field(alias="isApproveEnable")
    ] = None
    is_mint_schema: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isMintSchema"), pydantic.Field(alias="isMintSchema")
    ] = None
    mint_options: typing_extensions.Annotated[
        typing.Optional[WizardConfigSchemasItemMintOptions],
        FieldMetadata(alias="mintOptions"),
        pydantic.Field(alias="mintOptions"),
    ] = None
    dependency_schema_iri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="dependencySchemaIri"), pydantic.Field(alias="dependencySchemaIri")
    ] = None
    relationships_schema_iri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="relationshipsSchemaIri"),
        pydantic.Field(alias="relationshipsSchemaIri"),
    ] = None
    initial_roles_for: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="initialRolesFor"),
        pydantic.Field(alias="initialRolesFor"),
    ] = None
    roles_config: typing_extensions.Annotated[
        typing.Optional[typing.List[WizardConfigSchemasItemRolesConfigItem]],
        FieldMetadata(alias="rolesConfig"),
        pydantic.Field(alias="rolesConfig"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
