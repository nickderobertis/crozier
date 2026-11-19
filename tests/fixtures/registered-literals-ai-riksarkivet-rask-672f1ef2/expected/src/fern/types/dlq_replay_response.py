

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DlqReplayResponse(UniversalBaseModel):
    """
    The result of re-ingesting one staged event (#83): idempotent MERGE on ``run_id``, then drop.
    """

    run_id: str
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
