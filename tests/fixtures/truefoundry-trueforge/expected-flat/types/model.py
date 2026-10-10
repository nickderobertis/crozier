

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_params import ModelParams


class Model(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Model FQN: `provider/model`, e.g. `openai/gpt-5.2`.
    """

    params: typing.Optional[ModelParams] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
