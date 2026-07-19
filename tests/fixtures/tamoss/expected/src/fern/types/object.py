

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .object_core import ObjectCore
from .timerange import Timerange
from .uuid_ import Uuid


class Object(ObjectCore):
    id: str = pydantic.Field()
    """
    The Media Object identifier.
    """

    referenced_by_flows: typing.List[Uuid] = pydantic.Field()
    """
    List of Flows that reference this Media Object via Flow Segments in this store instance.
    """

    first_referenced_by_flow: typing.Optional[Uuid] = pydantic.Field(default=None)
    """
    The first Flow that had a Flow Segment reference the Media Object in this store instance. This Flow is also present in 'referenced_by_flows' if it is still referenced by the Flow. This property is optional and may in some implementations become unset if the Flow no longer references the media object, e.g. because it was deleted.
    """

    timerange: Timerange = pydantic.Field()
    """
    The timerange covering the sample timestamps embedded in or derived from the Media Object itself, on the Media Object's timeline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
