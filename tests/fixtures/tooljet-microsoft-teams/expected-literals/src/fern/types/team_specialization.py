

import typing

TeamSpecialization = typing.Union[
    typing.Literal[
        "none",
        "educationStandard",
        "educationClass",
        "educationProfessionalLearningCommunity",
        "educationStaff",
        "healthcareStandard",
        "healthcareCareCoordination",
        "unknownFutureValue",
    ],
    typing.Any,
]
