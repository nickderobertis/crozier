

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EtcdKeyRotationStatusPhase(enum.StrEnum):
    """
    The last entered phase, which a failure retains. A `prepare` failure releases the mutation lock, so start a new rotation workflow after fixing it; a failure in a later phase keeps the lock for recovery of the owning workflow.
    """

    PREPARE = "prepare"
    ADD_SECONDARY = "add_secondary"
    PROMOTE_PRIMARY = "promote_primary"
    REWRITE = "rewrite"
    REMOVE_OLD_KEYS = "remove_old_keys"
    FINALIZE = "finalize"

    def visit(
        self,
        prepare: typing.Callable[[], T_Result],
        add_secondary: typing.Callable[[], T_Result],
        promote_primary: typing.Callable[[], T_Result],
        rewrite: typing.Callable[[], T_Result],
        remove_old_keys: typing.Callable[[], T_Result],
        finalize: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EtcdKeyRotationStatusPhase.PREPARE:
            return prepare()
        if self is EtcdKeyRotationStatusPhase.ADD_SECONDARY:
            return add_secondary()
        if self is EtcdKeyRotationStatusPhase.PROMOTE_PRIMARY:
            return promote_primary()
        if self is EtcdKeyRotationStatusPhase.REWRITE:
            return rewrite()
        if self is EtcdKeyRotationStatusPhase.REMOVE_OLD_KEYS:
            return remove_old_keys()
        if self is EtcdKeyRotationStatusPhase.FINALIZE:
            return finalize()
