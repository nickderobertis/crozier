

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .trust_rule_suggest_response_suggestion_directory_scope_options_item import (
    TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem,
)
from .trust_rule_suggest_response_suggestion_scope_options_item import (
    TrustRuleSuggestResponseSuggestionScopeOptionsItem,
)


class TrustRuleSuggestResponseSuggestion(UniversalBaseModel):
    pattern: str
    risk: str
    scope: typing.Optional[str] = None
    description: str
    scope_options: typing_extensions.Annotated[
        typing.List[TrustRuleSuggestResponseSuggestionScopeOptionsItem],
        FieldMetadata(alias="scopeOptions"),
        pydantic.Field(alias="scopeOptions"),
    ]
    directory_scope_options: typing_extensions.Annotated[
        typing.Optional[typing.List[TrustRuleSuggestResponseSuggestionDirectoryScopeOptionsItem]],
        FieldMetadata(alias="directoryScopeOptions"),
        pydantic.Field(alias="directoryScopeOptions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
