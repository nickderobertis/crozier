

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokensIssueRequestTenantScopeItemOne(enum.StrEnum):
    DOCS_CREATE = "docs.create"
    DOCS_READ = "docs.read"
    DOCS_DELETE = "docs.delete"
    TOKENS_ISSUE_DOC = "tokens.issue-doc"
    TOKENS_REVOKE = "tokens.revoke"
    SHARES_MANAGE = "shares.manage"

    def visit(
        self,
        docs_create: typing.Callable[[], T_Result],
        docs_read: typing.Callable[[], T_Result],
        docs_delete: typing.Callable[[], T_Result],
        tokens_issue_doc: typing.Callable[[], T_Result],
        tokens_revoke: typing.Callable[[], T_Result],
        shares_manage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TokensIssueRequestTenantScopeItemOne.DOCS_CREATE:
            return docs_create()
        if self is TokensIssueRequestTenantScopeItemOne.DOCS_READ:
            return docs_read()
        if self is TokensIssueRequestTenantScopeItemOne.DOCS_DELETE:
            return docs_delete()
        if self is TokensIssueRequestTenantScopeItemOne.TOKENS_ISSUE_DOC:
            return tokens_issue_doc()
        if self is TokensIssueRequestTenantScopeItemOne.TOKENS_REVOKE:
            return tokens_revoke()
        if self is TokensIssueRequestTenantScopeItemOne.SHARES_MANAGE:
            return shares_manage()
