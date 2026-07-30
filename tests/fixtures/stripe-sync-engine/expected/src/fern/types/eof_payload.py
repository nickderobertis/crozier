

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .progress_payload import ProgressPayload
from .run_status import RunStatus
from .sync_state import SyncState


class EofPayload(UniversalBaseModel):
    """
    Deprecated terminal message signaling end of this request. Prefer explicit request/response results via pipeline_sync_batch.
    """

    status: RunStatus = pydantic.Field()
    """
    Terminal run status derived from stream outcomes.
    """

    has_more: bool = pydantic.Field()
    """
    Whether the client should continue with another request. true when cut off by limits; false when the source iterator exhausted naturally.
    """

    ending_state: typing.Optional[SyncState] = pydantic.Field(default=None)
    """
    Full sync state at the end of this request. Round-trip this as starting_state on the next request.
    """

    run_progress: ProgressPayload = pydantic.Field()
    """
    Accumulated progress across all requests in this sync run.
    """

    request_progress: ProgressPayload = pydantic.Field()
    """
    Progress for this specific request only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
