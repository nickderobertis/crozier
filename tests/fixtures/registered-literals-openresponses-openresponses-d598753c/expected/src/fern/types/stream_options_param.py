

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StreamOptionsParam(UniversalBaseModel):
    """
    Options that control streamed response behavior.
    """

    include_obfuscation: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to obfuscate sensitive information in streamed output. Defaults to `true`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
