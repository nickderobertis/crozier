

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PipelineGetByNumberResponseVcsCommit(UniversalBaseModel):
    """
    The latest commit in the pipeline.
    """

    subject: str = pydantic.Field()
    """
    The subject of the commit message.
    """

    body: str = pydantic.Field()
    """
    The body of the commit message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
