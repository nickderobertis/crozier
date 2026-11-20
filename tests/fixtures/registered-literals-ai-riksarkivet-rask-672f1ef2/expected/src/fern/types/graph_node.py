

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GraphNode(UniversalBaseModel):
    """
    A dataset node in the lineage graph (``id`` is the catalog table id).

    ``source_uri`` is where the table physically lives (the S3-compatible location, from
    the ``dataSource`` facet) and ``tags`` are its governance labels (from the ``tags`` facet).
    """

    failed: typing.Optional[bool] = None
    id: str
    kind: typing.Optional[str] = None
    namespace: typing.Optional[str] = None
    source_uri: typing.Optional[str] = None
    tags: typing.Optional[typing.List[str]] = None
    versions: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
