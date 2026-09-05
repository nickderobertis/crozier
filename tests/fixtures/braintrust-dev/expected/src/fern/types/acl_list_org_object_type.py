

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AclListOrgObjectType(enum.StrEnum):
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
        if self is AclListOrgObjectType.ORGANIZATION:
            return organization()
        if self is AclListOrgObjectType.PROJECT:
            return project()
        if self is AclListOrgObjectType.EXPERIMENT:
            return experiment()
        if self is AclListOrgObjectType.DATASET:
            return dataset()
        if self is AclListOrgObjectType.PROMPT:
            return prompt()
        if self is AclListOrgObjectType.PROMPT_SESSION:
            return prompt_session()
        if self is AclListOrgObjectType.GROUP:
            return group()
        if self is AclListOrgObjectType.ROLE:
            return role()
        if self is AclListOrgObjectType.ORG_MEMBER:
            return org_member()
        if self is AclListOrgObjectType.PROJECT_LOG:
            return project_log()
        if self is AclListOrgObjectType.ORG_PROJECT:
            return org_project()
