

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenAiPartialParams(UniversalBaseModel):
    model_id: typing.Optional[str] = None
    prompt_template: typing.Optional[str] = None
    params: typing.Optional[typing.Dict[str, typing.Any]] = None
    timeout: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
