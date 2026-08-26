

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AiModelConfig(UniversalBaseModel):
    """
    Configuration options for an AI model.

        **Keys.**

        - `chat_model`: the model to use for chat completions
        - `edit_model`: the model to use for edit completions
        - `autocomplete_model`: the model to use for code completion/autocomplete
        - `displayed_models`: a list of models to display in the UI
        - `custom_models`: a list of custom models to use that are not from the default list
    """

    autocomplete_model: typing.Optional[str] = None
    chat_model: typing.Optional[str] = None
    custom_models: typing.List[str]
    displayed_models: typing.List[str]
    edit_model: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
