

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostTagsSynchronizationRequestEntity(enum.StrEnum):
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
        if self is PostTagsSynchronizationRequestEntity.SCHEMA:
            return schema()
        if self is PostTagsSynchronizationRequestEntity.POLICY:
            return policy()
        if self is PostTagsSynchronizationRequestEntity.TOKEN:
            return token()
        if self is PostTagsSynchronizationRequestEntity.MODULE:
            return module()
        if self is PostTagsSynchronizationRequestEntity.CONTRACT:
            return contract()
        if self is PostTagsSynchronizationRequestEntity.POLICY_DOCUMENT:
            return policy_document()
