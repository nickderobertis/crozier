

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rule import Rule
from .rule_set_enable_at import RuleSetEnableAt


class RuleSet(UniversalBaseModel):
    """
    Schema rule set
    """

    migration_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[Rule]],
        FieldMetadata(alias="migrationRules"),
        pydantic.Field(alias="migrationRules"),
    ] = None
    domain_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[Rule]], FieldMetadata(alias="domainRules"), pydantic.Field(alias="domainRules")
    ] = None
    encoding_rules: typing_extensions.Annotated[
        typing.Optional[typing.List[Rule]], FieldMetadata(alias="encodingRules"), pydantic.Field(alias="encodingRules")
    ] = None
    enable_at: typing_extensions.Annotated[
        typing.Optional[RuleSetEnableAt], FieldMetadata(alias="enableAt"), pydantic.Field(alias="enableAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
