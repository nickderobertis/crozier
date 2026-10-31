

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmbedResponse(UniversalBaseModel):
    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model that produced the embeddings
    """

    embeddings: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    Array of vector embeddings
    """

    total_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time spent generating in nanoseconds
    """

    load_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Load time in nanoseconds
    """

    prompt_eval_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of input tokens processed to generate embeddings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
