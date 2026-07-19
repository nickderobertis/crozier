

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CodeInput(UniversalBaseModel):
    code: str = pydantic.Field()
    """
    Source code to parse for JSON schema
    """

    source_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source type of the code (python or typescript)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
