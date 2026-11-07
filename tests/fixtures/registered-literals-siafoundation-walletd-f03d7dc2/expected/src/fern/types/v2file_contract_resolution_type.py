

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2FileContractResolutionType(enum.StrEnum):
    RENEWAL = "renewal"
    STORAGE_PROOF = "storageProof"
    EXPIRATION = "expiration"

    def visit(
        self,
        renewal: typing.Callable[[], T_Result],
        storage_proof: typing.Callable[[], T_Result],
        expiration: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2FileContractResolutionType.RENEWAL:
            return renewal()
        if self is V2FileContractResolutionType.STORAGE_PROOF:
            return storage_proof()
        if self is V2FileContractResolutionType.EXPIRATION:
            return expiration()
