

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .federation_node_status import FederationNodeStatus


class FederationNode(UniversalBaseModel):
    node_id: str
    status: FederationNodeStatus
    capabilities: typing.Optional[typing.List[str]] = None
    latency_ms: typing.Optional[int] = None
    load_score: typing.Optional[int] = None
    trust_score: typing.Optional[float] = None
    quarantined: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
