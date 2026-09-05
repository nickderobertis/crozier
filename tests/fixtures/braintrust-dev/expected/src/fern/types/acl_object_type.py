

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AclObjectType(enum.StrEnum):
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
        if self is AclObjectType.ORGANIZATION:
            return organization()
        if self is AclObjectType.PROJECT:
            return project()
        if self is AclObjectType.EXPERIMENT:
            return experiment()
        if self is AclObjectType.DATASET:
            return dataset()
        if self is AclObjectType.PROMPT:
            return prompt()
        if self is AclObjectType.PROMPT_SESSION:
            return prompt_session()
        if self is AclObjectType.GROUP:
            return group()
        if self is AclObjectType.ROLE:
            return role()
        if self is AclObjectType.ORG_MEMBER:
            return org_member()
        if self is AclObjectType.PROJECT_LOG:
            return project_log()
        if self is AclObjectType.ORG_PROJECT:
            return org_project()
