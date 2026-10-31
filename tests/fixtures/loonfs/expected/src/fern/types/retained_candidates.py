

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetainedCandidates(UniversalBaseModel):
    """
    The candidates that one garbage collection pass inspected but didn't delete, counted by reason.
    """

    checkpoint_not_deletable: int = pydantic.Field()
    """
    The checkpoint records that the pass couldn't delete because of their owner or their grace
    window.
    """

    no_provider_timestamp: int = pydantic.Field()
    """
    The unreferenced candidates that had no provider timestamp, so their age was unknown.
    """

    referenced: int = pydantic.Field()
    """
    The candidates that a current root or the shared base filter protected, or that manifest
    discovery needed.
    """

    unrecognized_key: int = pydantic.Field()
    """
    The keys that garbage collection didn't recognize in the object families it scanned. The
    pass keeps these objects.
    """

    upload_session_undecided: int = pydantic.Field()
    """
    The upload sessions that the pass couldn't prove safe to delete.
    """

    upload_session_window: int = pydantic.Field()
    """
    The upload sessions that a lease or grace window still protected.
    """

    within_grace_window: int = pydantic.Field()
    """
    The unreferenced candidates that were younger than the grace window, according to their
    provider timestamps.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
