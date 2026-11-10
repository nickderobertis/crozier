

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostTagsSearchRequestTargetEntity(enum.StrEnum):
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
        if self is PostTagsSearchRequestTargetEntity.SCHEMA:
            return schema()
        if self is PostTagsSearchRequestTargetEntity.POLICY:
            return policy()
        if self is PostTagsSearchRequestTargetEntity.TOKEN:
            return token()
        if self is PostTagsSearchRequestTargetEntity.MODULE:
            return module()
        if self is PostTagsSearchRequestTargetEntity.CONTRACT:
            return contract()
        if self is PostTagsSearchRequestTargetEntity.POLICY_DOCUMENT:
            return policy_document()
