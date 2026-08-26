

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completion_config_copilot import CompletionConfigCopilot


class CompletionConfig(UniversalBaseModel):
    """
    Configuration for code completion.

        A dict with key/value pairs configuring code completion in the marimo
        editor.

        **Keys.**

        - `activate_on_typing`: if `False`, completion won't activate
        until the completion hotkey is entered
        - `signature_hint_on_typing`: if `False`, signature hint won't be shown when typing
        - `copilot`: one of `"github"`, `"codeium"`, or `"custom"`
        - `codeium_api_key`: the Codeium API key
        - `auto_close_pairs`: if `False`, typing an opening bracket, parenthesis,
        or quote will not automatically insert the closing character
    """

    activate_on_typing: bool
    api_key: typing.Optional[str] = None
    auto_close_pairs: typing.Optional[bool] = None
    base_url: typing.Optional[str] = None
    codeium_api_key: typing.Optional[str] = None
    copilot: CompletionConfigCopilot
    model: typing.Optional[str] = None
    signature_hint_on_typing: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
