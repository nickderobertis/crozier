

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .config_update_request_compatibility import ConfigUpdateRequestCompatibility
from .metadata import Metadata
from .rule_set import RuleSet


class ConfigUpdateRequest(UniversalBaseModel):
    """
    Config update request
    """

    alias: typing.Optional[str] = None
    alias_for_deks: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="aliasForDeks"), pydantic.Field(alias="aliasForDeks")
    ] = None
    normalize: typing.Optional[bool] = None
    validate_fields: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="validateFields"), pydantic.Field(alias="validateFields")
    ] = None
    validate_new_schemas: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="validateNewSchemas"), pydantic.Field(alias="validateNewSchemas")
    ] = None
    validate_rules: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="validateRules"), pydantic.Field(alias="validateRules")
    ] = None
    compatibility: typing.Optional[ConfigUpdateRequestCompatibility] = pydantic.Field(default=None)
    """
    Compatibility Level
    """

    compatibility_policy: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="compatibilityPolicy"), pydantic.Field(alias="compatibilityPolicy")
    ] = None
    compatibility_group: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="compatibilityGroup"), pydantic.Field(alias="compatibilityGroup")
    ] = None
    default_metadata: typing_extensions.Annotated[
        typing.Optional[Metadata], FieldMetadata(alias="defaultMetadata"), pydantic.Field(alias="defaultMetadata")
    ] = None
    override_metadata: typing_extensions.Annotated[
        typing.Optional[Metadata], FieldMetadata(alias="overrideMetadata"), pydantic.Field(alias="overrideMetadata")
    ] = None
    default_rule_set: typing_extensions.Annotated[
        typing.Optional[RuleSet], FieldMetadata(alias="defaultRuleSet"), pydantic.Field(alias="defaultRuleSet")
    ] = None
    override_rule_set: typing_extensions.Annotated[
        typing.Optional[RuleSet], FieldMetadata(alias="overrideRuleSet"), pydantic.Field(alias="overrideRuleSet")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
