

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq


class RunMaintenanceRequestRetention(UniversalBaseModel):
    """
    A job that advances the retention floor toward the folded manifest head, or toward the
    target that the request sets.

    The floor doesn't pass a commit that's less than one hour old.
    """

    cutoff_at_ms: typing.Optional[int] = pydantic.Field(default=None)
    """
    A Unix time in milliseconds. The floor advances to the last commit made at or before this
    time. LoonFS reads commits upward from the floor, and the first commit made after this time
    ends the advance. This field can't be combined with `to_seq`.
    """

    to_seq: typing.Optional[ChangeSeq] = pydantic.Field(default=None)
    """
    The sequence to advance the floor to. If the folded manifest head is lower, the floor
    advances to the head instead. This field can't be combined with `cutoff_at_ms`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
