

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunInput(UniversalBaseModel):
    """
    One dataset a run consumed, with the PINNED version it read (``None`` = read floating LATEST).

    The version is the OpenLineage ``version`` facet the producer stamped on the input — the Ray TRAIN
    job pins every feature (#115 D1: training on floating LATEST is not reproducible). It rides the
    graph's ``READ`` edge; this is the API surface for it (before, it was reachable only by Cypher).
    """

    name: str
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
