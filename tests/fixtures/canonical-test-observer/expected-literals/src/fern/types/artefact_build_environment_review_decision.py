

import typing

ArtefactBuildEnvironmentReviewDecision = typing.Union[
    typing.Literal[
        "REJECTED",
        "APPROVED_INCONSISTENT_TEST",
        "APPROVED_UNSTABLE_PHYSICAL_INFRA",
        "APPROVED_CUSTOMER_PREREQUISITE_FAIL",
        "APPROVED_FAULTY_HARDWARE",
        "APPROVED_ALL_TESTS_PASS",
    ],
    typing.Any,
]
