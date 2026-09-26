

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileContent(UniversalBaseModel):
    data: str = pydantic.Field()
    """
    Data URI: `data:<mime>;base64,<payload>`. MIME type is parsed from the URI.
    """

    name: str = pydantic.Field()
    """
    Filename presented to the agent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
