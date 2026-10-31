

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Permission(enum.StrEnum):
    VIEW_USER = "view_user"
    CHANGE_USER = "change_user"
    VIEW_TEAM = "view_team"
    CHANGE_TEAM = "change_team"
    ADD_APPLICATION = "add_application"
    CHANGE_APPLICATION = "change_application"
    VIEW_APPLICATION = "view_application"
    VIEW_PERMISSION = "view_permission"
    VIEW_ISSUE = "view_issue"
    CHANGE_ISSUE = "change_issue"
    CHANGE_ISSUE_ATTACHMENT = "change_issue_attachment"
    CHANGE_ISSUE_ATTACHMENT_BULK = "change_issue_attachment_bulk"
    CHANGE_ATTACHMENT_RULE = "change_attachment_rule"
    CHANGE_AUTO_RERUN = "change_auto_rerun"
    VIEW_TEST = "view_test"
    CHANGE_TEST = "change_test"
    VIEW_RERUN = "view_rerun"
    CHANGE_RERUN = "change_rerun"
    CHANGE_RERUN_BULK = "change_rerun_bulk"
    VIEW_ARTEFACT = "view_artefact"
    CHANGE_ARTEFACT = "change_artefact"
    DELETE_ARTEFACT = "delete_artefact"
    VIEW_ENVIRONMENT_REVIEW = "view_environment_review"
    CHANGE_ENVIRONMENT_REVIEW = "change_environment_review"
    VIEW_REPORT = "view_report"
    VIEW_TEST_CASE_REPORTED_ISSUE = "view_test_case_reported_issue"
    CHANGE_TEST_CASE_REPORTED_ISSUE = "change_test_case_reported_issue"
    VIEW_ENVIRONMENT_REPORTED_ISSUE = "view_environment_reported_issue"
    CHANGE_ENVIRONMENT_REPORTED_ISSUE = "change_environment_reported_issue"
    VIEW_NOTIFICATION = "view_notification"
    CHANGE_NOTIFICATION = "change_notification"
    VIEW_SENTRY_DEBUG = "view_sentry_debug"

    def visit(
        self,
        view_user: typing.Callable[[], T_Result],
        change_user: typing.Callable[[], T_Result],
        view_team: typing.Callable[[], T_Result],
        change_team: typing.Callable[[], T_Result],
        add_application: typing.Callable[[], T_Result],
        change_application: typing.Callable[[], T_Result],
        view_application: typing.Callable[[], T_Result],
        view_permission: typing.Callable[[], T_Result],
        view_issue: typing.Callable[[], T_Result],
        change_issue: typing.Callable[[], T_Result],
        change_issue_attachment: typing.Callable[[], T_Result],
        change_issue_attachment_bulk: typing.Callable[[], T_Result],
        change_attachment_rule: typing.Callable[[], T_Result],
        change_auto_rerun: typing.Callable[[], T_Result],
        view_test: typing.Callable[[], T_Result],
        change_test: typing.Callable[[], T_Result],
        view_rerun: typing.Callable[[], T_Result],
        change_rerun: typing.Callable[[], T_Result],
        change_rerun_bulk: typing.Callable[[], T_Result],
        view_artefact: typing.Callable[[], T_Result],
        change_artefact: typing.Callable[[], T_Result],
        delete_artefact: typing.Callable[[], T_Result],
        view_environment_review: typing.Callable[[], T_Result],
        change_environment_review: typing.Callable[[], T_Result],
        view_report: typing.Callable[[], T_Result],
        view_test_case_reported_issue: typing.Callable[[], T_Result],
        change_test_case_reported_issue: typing.Callable[[], T_Result],
        view_environment_reported_issue: typing.Callable[[], T_Result],
        change_environment_reported_issue: typing.Callable[[], T_Result],
        view_notification: typing.Callable[[], T_Result],
        change_notification: typing.Callable[[], T_Result],
        view_sentry_debug: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Permission.VIEW_USER:
            return view_user()
        if self is Permission.CHANGE_USER:
            return change_user()
        if self is Permission.VIEW_TEAM:
            return view_team()
        if self is Permission.CHANGE_TEAM:
            return change_team()
        if self is Permission.ADD_APPLICATION:
            return add_application()
        if self is Permission.CHANGE_APPLICATION:
            return change_application()
        if self is Permission.VIEW_APPLICATION:
            return view_application()
        if self is Permission.VIEW_PERMISSION:
            return view_permission()
        if self is Permission.VIEW_ISSUE:
            return view_issue()
        if self is Permission.CHANGE_ISSUE:
            return change_issue()
        if self is Permission.CHANGE_ISSUE_ATTACHMENT:
            return change_issue_attachment()
        if self is Permission.CHANGE_ISSUE_ATTACHMENT_BULK:
            return change_issue_attachment_bulk()
        if self is Permission.CHANGE_ATTACHMENT_RULE:
            return change_attachment_rule()
        if self is Permission.CHANGE_AUTO_RERUN:
            return change_auto_rerun()
        if self is Permission.VIEW_TEST:
            return view_test()
        if self is Permission.CHANGE_TEST:
            return change_test()
        if self is Permission.VIEW_RERUN:
            return view_rerun()
        if self is Permission.CHANGE_RERUN:
            return change_rerun()
        if self is Permission.CHANGE_RERUN_BULK:
            return change_rerun_bulk()
        if self is Permission.VIEW_ARTEFACT:
            return view_artefact()
        if self is Permission.CHANGE_ARTEFACT:
            return change_artefact()
        if self is Permission.DELETE_ARTEFACT:
            return delete_artefact()
        if self is Permission.VIEW_ENVIRONMENT_REVIEW:
            return view_environment_review()
        if self is Permission.CHANGE_ENVIRONMENT_REVIEW:
            return change_environment_review()
        if self is Permission.VIEW_REPORT:
            return view_report()
        if self is Permission.VIEW_TEST_CASE_REPORTED_ISSUE:
            return view_test_case_reported_issue()
        if self is Permission.CHANGE_TEST_CASE_REPORTED_ISSUE:
            return change_test_case_reported_issue()
        if self is Permission.VIEW_ENVIRONMENT_REPORTED_ISSUE:
            return view_environment_reported_issue()
        if self is Permission.CHANGE_ENVIRONMENT_REPORTED_ISSUE:
            return change_environment_reported_issue()
        if self is Permission.VIEW_NOTIFICATION:
            return view_notification()
        if self is Permission.CHANGE_NOTIFICATION:
            return change_notification()
        if self is Permission.VIEW_SENTRY_DEBUG:
            return view_sentry_debug()
