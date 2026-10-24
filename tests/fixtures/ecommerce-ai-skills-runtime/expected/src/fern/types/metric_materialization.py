

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metric_materialization_quality_summary import MetricMaterializationQualitySummary
from .metric_materialization_status import MetricMaterializationStatus


class MetricMaterialization(UniversalBaseModel):
    id: str
    tenant_id: str
    evidence_import_id: str
    idempotency_key: str
    status: MetricMaterializationStatus
    observation_count: int
    quarantine_count: int
    currencies: typing.List[str] = pydantic.Field()
    """
    Explicit currencies present in accepted observations; values are never combined across entries.
    """

    quality_summary: MetricMaterializationQualitySummary
    error_code: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    created_by: str
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
