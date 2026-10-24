

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proposal_capability_block import ProposalCapabilityBlock
from .proposal_execution_status import ProposalExecutionStatus
from .proposal_operation import ProposalOperation


class ProposalExecution(UniversalBaseModel):
    id: str
    tenant_id: str
    proposal_id: str
    proposal_version: int
    approved_payload_hash: str
    approved_content_hash: str
    idempotency_key: str
    operation: ProposalOperation
    status: ProposalExecutionStatus
    action_id: typing.Optional[str] = None
    lease_until: typing.Optional[dt.datetime] = None
    attempt_count: int
    max_attempts: int
    result: typing.Optional[typing.Dict[str, typing.Any]] = None
    error_code: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    last_retry_idempotency_key: typing.Optional[str] = None
    created_by: str
    created_at: dt.datetime
    updated_at: dt.datetime
    completed_at: typing.Optional[dt.datetime] = None
    capability_block: typing.Optional[ProposalCapabilityBlock] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
