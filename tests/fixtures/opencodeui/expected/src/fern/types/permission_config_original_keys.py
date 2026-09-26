

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .permission_action_config import PermissionActionConfig
from .permission_rule_config import PermissionRuleConfig


class PermissionConfigOriginalKeys(UniversalBaseModel):
    original_keys: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="__originalKeys"), pydantic.Field(alias="__originalKeys")
    ] = None
    read: typing.Optional[PermissionRuleConfig] = None
    edit: typing.Optional[PermissionRuleConfig] = None
    glob: typing.Optional[PermissionRuleConfig] = None
    grep: typing.Optional[PermissionRuleConfig] = None
    list_: typing_extensions.Annotated[
        typing.Optional[PermissionRuleConfig], FieldMetadata(alias="list"), pydantic.Field(alias="list")
    ] = None
    bash: typing.Optional[PermissionRuleConfig] = None
    task: typing.Optional[PermissionRuleConfig] = None
    external_directory: typing.Optional[PermissionRuleConfig] = None
    todowrite: typing.Optional[PermissionActionConfig] = None
    todoread: typing.Optional[PermissionActionConfig] = None
    question: typing.Optional[PermissionActionConfig] = None
    webfetch: typing.Optional[PermissionActionConfig] = None
    websearch: typing.Optional[PermissionActionConfig] = None
    codesearch: typing.Optional[PermissionActionConfig] = None
    lsp: typing.Optional[PermissionRuleConfig] = None
    doom_loop: typing.Optional[PermissionActionConfig] = None
    skill: typing.Optional[PermissionRuleConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
