

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .evidence_report_type import EvidenceReportType
from .marketplace_id import MarketplaceId


class EvidenceImport(UniversalBaseModel):
    id: str
    tenant_id: str
    idempotency_key: str
    platform: MarketplaceId
    report_type: EvidenceReportType
    filename: str
    observed_at: dt.datetime
    sha256: str
    delimiter: str
    row_count: int
    blank_rows_skipped: int
    formula_cells: int
    columns: typing.List[str]
    column_mapping: typing.Dict[str, str]
    media_type: typing.Optional[str] = None
    byte_size: typing.Optional[int] = None
    object_key: typing.Optional[str] = None
    sheet_name: typing.Optional[str] = None
    created_by: str
    created_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
