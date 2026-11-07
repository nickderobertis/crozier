

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProcessorDefinitionDto(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the processor (externalized or scheduled)
    """

    name: str = pydantic.Field()
    """
    Name of the processor
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
