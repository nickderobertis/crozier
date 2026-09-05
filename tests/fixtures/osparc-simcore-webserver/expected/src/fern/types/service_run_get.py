

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_transaction_status import CreditTransactionStatus
from .service_run_status import ServiceRunStatus
from .user_id_int import UserIdInt
from .wallet_id_int import WalletIdInt


class ServiceRunGet(UniversalBaseModel):
    service_run_id: str
    wallet_id: typing.Optional[WalletIdInt] = None
    wallet_name: typing.Optional[str] = None
    user_id: UserIdInt
    user_email: str
    project_id: str
    project_name: str
    project_tags: typing.List[str]
    node_id: str
    node_name: str
    root_parent_project_id: str
    root_parent_project_name: str
    service_key: str
    service_version: str
    service_type: str
    started_at: dt.datetime
    stopped_at: typing.Optional[dt.datetime] = None
    service_run_status: ServiceRunStatus
    credit_cost: typing.Optional[str] = None
    transaction_status: typing.Optional[CreditTransactionStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
