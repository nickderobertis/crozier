

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from .lemur_base_params import LemurBaseParams


class LemurActionItemsParams(LemurBaseParams):
    answer_format: typing.Optional[str] = pydantic.Field(default=None)
    """
    How you want the action items to be returned. This can be any text.
    Defaults to "Bullet Points".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
