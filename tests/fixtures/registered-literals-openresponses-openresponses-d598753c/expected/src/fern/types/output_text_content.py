

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotation import Annotation
from .log_prob import LogProb


class OutputTextContent(UniversalBaseModel):
    """
    A text output from the model.
    """

    text: str = pydantic.Field()
    """
    The text output from the model.
    """

    annotations: typing.List[Annotation] = pydantic.Field()
    """
    The annotations of the text output.
    """

    logprobs: typing.Optional[typing.List[LogProb]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
