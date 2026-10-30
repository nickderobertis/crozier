

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segment_state import SegmentState


class Segment(UniversalBaseModel):
    """
    The segment object
    """

    segment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of this segment
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the list to which the segment belongs
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account timezone used for datetime fields
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the segment
    """

    definition: typing.Optional[str] = pydantic.Field(default=None)
    """
    The definition of the segment (string in JSON format)
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time of creation
    """

    created_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time of creation in ISO format
    """

    modified: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time of last modification
    """

    modified_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Time of last modification in ISO format
    """

    state: typing.Optional[SegmentState] = pydantic.Field(default=None)
    """
    The state of this segment: active or deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
