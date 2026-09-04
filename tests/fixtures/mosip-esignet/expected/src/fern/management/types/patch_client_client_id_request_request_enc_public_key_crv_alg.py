

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyCrvAlg(enum.StrEnum):
    """
    Algorithm for key management
    """

    ECDH_ES = "ECDH-ES"
    ECDH_ES_A128KW = "ECDH-ES+A128KW"
    ECDH_ES_A192KW = "ECDH-ES+A192KW"
    ECDH_ES_A256KW = "ECDH-ES+A256KW"

    def visit(
        self,
        ecdh_es: typing.Callable[[], T_Result],
        ecdh_es_a128kw: typing.Callable[[], T_Result],
        ecdh_es_a192kw: typing.Callable[[], T_Result],
        ecdh_es_a256kw: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvAlg.ECDH_ES:
            return ecdh_es()
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvAlg.ECDH_ES_A128KW:
            return ecdh_es_a128kw()
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvAlg.ECDH_ES_A192KW:
            return ecdh_es_a192kw()
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvAlg.ECDH_ES_A256KW:
            return ecdh_es_a256kw()
