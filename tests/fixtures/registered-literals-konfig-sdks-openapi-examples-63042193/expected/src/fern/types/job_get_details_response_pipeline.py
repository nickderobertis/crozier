

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetDetailsResponsePipeline(UniversalBaseModel):
    """
    Info about a pipeline the job is a part of.
    """

    id: str = pydantic.Field()
    """
    The unique ID of the pipeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
