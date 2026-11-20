

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GraphEdge(UniversalBaseModel):
    """
    A dataset-level lineage edge: ``source`` is derived from ``target``.
    """

    kind: typing.Optional[str] = None
    source: str
    target: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
