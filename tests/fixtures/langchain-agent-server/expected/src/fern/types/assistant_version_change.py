

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssistantVersionChange(UniversalBaseModel):
    """
    Payload for changing the version of an assistant.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The assistant version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
