

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .balance_sheet_assets import BalanceSheetAssets
from .balance_sheet_equity import BalanceSheetEquity
from .balance_sheet_liabilities import BalanceSheetLiabilities
from .created_at import CreatedAt
from .created_by import CreatedBy
from .id import Id
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class BalanceSheet(UniversalBaseModel):
    assets: BalanceSheetAssets
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of the report
    """

    equity: BalanceSheetEquity
    id: typing.Optional[Id] = None
    liabilities: BalanceSheetLiabilities
    report_name: str = pydantic.Field()
    """
    The name of the report
    """

    start_date: str = pydantic.Field()
    """
    The start date of the report
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
