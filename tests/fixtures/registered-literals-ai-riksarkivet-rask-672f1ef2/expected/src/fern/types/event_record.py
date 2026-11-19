

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventRecord(UniversalBaseModel):
    """
    One ingested OpenLineage event, Marquez-style (summary + the full event with facets).
    """

    author: typing.Optional[str] = None
    event: typing.Dict[str, typing.Any]
    event_time: typing.Optional[str] = None
    event_type: typing.Optional[str] = None
    inputs: typing.Optional[typing.List[str]] = None
    job: typing.Optional[str] = None
    outputs: typing.Optional[typing.List[str]] = None
    seq: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
