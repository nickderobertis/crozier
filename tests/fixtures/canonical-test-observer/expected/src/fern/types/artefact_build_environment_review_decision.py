

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArtefactBuildEnvironmentReviewDecision(enum.StrEnum):
    REJECTED = "REJECTED"
    APPROVED_INCONSISTENT_TEST = "APPROVED_INCONSISTENT_TEST"
    APPROVED_UNSTABLE_PHYSICAL_INFRA = "APPROVED_UNSTABLE_PHYSICAL_INFRA"
    APPROVED_CUSTOMER_PREREQUISITE_FAIL = "APPROVED_CUSTOMER_PREREQUISITE_FAIL"
    APPROVED_FAULTY_HARDWARE = "APPROVED_FAULTY_HARDWARE"
    APPROVED_ALL_TESTS_PASS = "APPROVED_ALL_TESTS_PASS"

    def visit(
        self,
        rejected: typing.Callable[[], T_Result],
        approved_inconsistent_test: typing.Callable[[], T_Result],
        approved_unstable_physical_infra: typing.Callable[[], T_Result],
        approved_customer_prerequisite_fail: typing.Callable[[], T_Result],
        approved_faulty_hardware: typing.Callable[[], T_Result],
        approved_all_tests_pass: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArtefactBuildEnvironmentReviewDecision.REJECTED:
            return rejected()
        if self is ArtefactBuildEnvironmentReviewDecision.APPROVED_INCONSISTENT_TEST:
            return approved_inconsistent_test()
        if self is ArtefactBuildEnvironmentReviewDecision.APPROVED_UNSTABLE_PHYSICAL_INFRA:
            return approved_unstable_physical_infra()
        if self is ArtefactBuildEnvironmentReviewDecision.APPROVED_CUSTOMER_PREREQUISITE_FAIL:
            return approved_customer_prerequisite_fail()
        if self is ArtefactBuildEnvironmentReviewDecision.APPROVED_FAULTY_HARDWARE:
            return approved_faulty_hardware()
        if self is ArtefactBuildEnvironmentReviewDecision.APPROVED_ALL_TESTS_PASS:
            return approved_all_tests_pass()
