

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PortfolioSyncRequestTransferType(enum.StrEnum):
    FULL_PORTFOLIO_MIGRATION = "full_portfolio_migration"
    PARTIAL_PORTFOLIO_MIGRATION = "partial_portfolio_migration"
    DATA_SYNC_ONLY = "data_sync_only"

    def visit(
        self,
        full_portfolio_migration: typing.Callable[[], T_Result],
        partial_portfolio_migration: typing.Callable[[], T_Result],
        data_sync_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PortfolioSyncRequestTransferType.FULL_PORTFOLIO_MIGRATION:
            return full_portfolio_migration()
        if self is PortfolioSyncRequestTransferType.PARTIAL_PORTFOLIO_MIGRATION:
            return partial_portfolio_migration()
        if self is PortfolioSyncRequestTransferType.DATA_SYNC_ONLY:
            return data_sync_only()
