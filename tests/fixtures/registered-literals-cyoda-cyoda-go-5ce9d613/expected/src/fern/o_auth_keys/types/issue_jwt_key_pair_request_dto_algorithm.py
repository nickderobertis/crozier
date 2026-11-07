

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class IssueJwtKeyPairRequestDtoAlgorithm(enum.StrEnum):
    RS256 = "RS256"
    RS384 = "RS384"
    RS512 = "RS512"
    ES256 = "ES256"
    ES384 = "ES384"
    ES512 = "ES512"
    PS256 = "PS256"
    PS384 = "PS384"
    PS512 = "PS512"
    ED_DSA = "EdDSA"

    def visit(
        self,
        rs256: typing.Callable[[], T_Result],
        rs384: typing.Callable[[], T_Result],
        rs512: typing.Callable[[], T_Result],
        es256: typing.Callable[[], T_Result],
        es384: typing.Callable[[], T_Result],
        es512: typing.Callable[[], T_Result],
        ps256: typing.Callable[[], T_Result],
        ps384: typing.Callable[[], T_Result],
        ps512: typing.Callable[[], T_Result],
        ed_dsa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IssueJwtKeyPairRequestDtoAlgorithm.RS256:
            return rs256()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.RS384:
            return rs384()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.RS512:
            return rs512()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.ES256:
            return es256()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.ES384:
            return es384()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.ES512:
            return es512()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.PS256:
            return ps256()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.PS384:
            return ps384()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.PS512:
            return ps512()
        if self is IssueJwtKeyPairRequestDtoAlgorithm.ED_DSA:
            return ed_dsa()
