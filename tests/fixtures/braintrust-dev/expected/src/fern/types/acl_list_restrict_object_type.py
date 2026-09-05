

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AclListRestrictObjectType(enum.StrEnum):
    """
    The object type that the ACL applies to
    """

    ORGANIZATION = "organization"
    PROJECT = "project"
    EXPERIMENT = "experiment"
    DATASET = "dataset"
    PROMPT = "prompt"
    PROMPT_SESSION = "prompt_session"
    GROUP = "group"
    ROLE = "role"
    ORG_MEMBER = "org_member"
    PROJECT_LOG = "project_log"
    ORG_PROJECT = "org_project"

    def visit(
        self,
        organization: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        experiment: typing.Callable[[], T_Result],
        dataset: typing.Callable[[], T_Result],
        prompt: typing.Callable[[], T_Result],
        prompt_session: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        role: typing.Callable[[], T_Result],
        org_member: typing.Callable[[], T_Result],
        project_log: typing.Callable[[], T_Result],
        org_project: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AclListRestrictObjectType.ORGANIZATION:
            return organization()
        if self is AclListRestrictObjectType.PROJECT:
            return project()
        if self is AclListRestrictObjectType.EXPERIMENT:
            return experiment()
        if self is AclListRestrictObjectType.DATASET:
            return dataset()
        if self is AclListRestrictObjectType.PROMPT:
            return prompt()
        if self is AclListRestrictObjectType.PROMPT_SESSION:
            return prompt_session()
        if self is AclListRestrictObjectType.GROUP:
            return group()
        if self is AclListRestrictObjectType.ROLE:
            return role()
        if self is AclListRestrictObjectType.ORG_MEMBER:
            return org_member()
        if self is AclListRestrictObjectType.PROJECT_LOG:
            return project_log()
        if self is AclListRestrictObjectType.ORG_PROJECT:
            return org_project()
