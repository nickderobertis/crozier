

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerateDuetRequestScriptItem(UniversalBaseModel):
    speaker: int = pydantic.Field()
    """
    Speaker index (0 or 1)
    """

    text: str = pydantic.Field()
    """
    Text for this speaker
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
