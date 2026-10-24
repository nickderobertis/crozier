

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MissionEventMetadata(UniversalBaseModel):
    """
    Bounded safe relationship/status metadata only, never a resource representation.
    """

    origin: typing.Optional[str] = None
    review_status: typing.Optional[str] = None
    attempt_count: typing.Optional[int] = None
    run_id: typing.Optional[str] = None
    recipe_id: typing.Optional[str] = None
    connector_account_id: typing.Optional[str] = None
    kind: typing.Optional[str] = None
    schedule_id: typing.Optional[str] = None
    daily_ops_run_id: typing.Optional[str] = None
    agent_run_id: typing.Optional[str] = None
    current_version: typing.Optional[int] = None
    priority_rank: typing.Optional[int] = None
    proposal_id: typing.Optional[str] = None
    proposal_version: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
