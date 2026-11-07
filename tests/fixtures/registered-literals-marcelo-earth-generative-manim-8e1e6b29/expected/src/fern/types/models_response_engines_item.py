

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .models_response_engines_item_engine import ModelsResponseEnginesItemEngine
from .models_response_engines_item_models_item import ModelsResponseEnginesItemModelsItem


class ModelsResponseEnginesItem(UniversalBaseModel):
    engine: ModelsResponseEnginesItemEngine
    configured: bool = pydantic.Field()
    """
    True if the corresponding API key environment variable is set.
    """

    default: str = pydantic.Field()
    """
    Default model ID used when no model is specified.
    """

    models: typing.List[ModelsResponseEnginesItemModelsItem]
    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional extra context (e.g. for LiteLLM's open model string format).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
