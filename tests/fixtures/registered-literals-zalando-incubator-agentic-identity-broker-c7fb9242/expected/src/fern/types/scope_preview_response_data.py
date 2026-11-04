

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScopePreviewResponseData(UniversalBaseModel):
    tool_pattern: str = pydantic.Field()
    """
    Server-derived exact matcher for the reviewed `tool_name`.
    """

    params_pattern: typing.Dict[str, str]
    preview: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
