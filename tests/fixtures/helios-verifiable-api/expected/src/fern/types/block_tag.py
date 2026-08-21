

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BlockTag(enum.StrEnum):
    """
    `earliest`: The lowest numbered block the client has available; `finalized`: The most recent crypto-economically secure block, cannot be re-orged outside of manual intervention driven by community coordination; `safe`: The most recent block that is safe from re-orgs under honest majority and certain synchronicity assumptions; `latest`: The most recent block in the canonical chain observed by the client, this block may be re-orged out of the canonical chain even under healthy/normal conditions; `pending`: A sample next block built by the client on top of `latest` and containing the set of transactions usually taken from local mempool. Before the merge transition is finalized, any call querying for `finalized` or `safe` block MUST be responded to with `-39001: Unknown block` error
    """

    EARLIEST = "earliest"
    FINALIZED = "finalized"
    SAFE = "safe"
    LATEST = "latest"
    PENDING = "pending"

    def visit(
        self,
        earliest: typing.Callable[[], T_Result],
        finalized: typing.Callable[[], T_Result],
        safe: typing.Callable[[], T_Result],
        latest: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BlockTag.EARLIEST:
            return earliest()
        if self is BlockTag.FINALIZED:
            return finalized()
        if self is BlockTag.SAFE:
            return safe()
        if self is BlockTag.LATEST:
            return latest()
        if self is BlockTag.PENDING:
            return pending()
