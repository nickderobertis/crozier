

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagEntity(enum.StrEnum):
    SCHEMA = "Schema"
    POLICY = "Policy"
    TOKEN = "Token"
    MODULE = "Module"
    CONTRACT = "Contract"
    POLICY_DOCUMENT = "PolicyDocument"

    def visit(
        self,
        schema: typing.Callable[[], T_Result],
        policy: typing.Callable[[], T_Result],
        token: typing.Callable[[], T_Result],
        module: typing.Callable[[], T_Result],
        contract: typing.Callable[[], T_Result],
        policy_document: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TagEntity.SCHEMA:
            return schema()
        if self is TagEntity.POLICY:
            return policy()
        if self is TagEntity.TOKEN:
            return token()
        if self is TagEntity.MODULE:
            return module()
        if self is TagEntity.CONTRACT:
            return contract()
        if self is TagEntity.POLICY_DOCUMENT:
            return policy_document()
