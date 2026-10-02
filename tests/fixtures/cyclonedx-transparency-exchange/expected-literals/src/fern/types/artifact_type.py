

import typing

ArtifactType = typing.Union[
    typing.Literal[
        "ATTESTATION",
        "BOM",
        "BUILD_META",
        "CERTIFICATION",
        "FORMULATION",
        "LICENSE",
        "RELEASE_NOTES",
        "SECURITY_TXT",
        "THREAT_MODEL",
        "VULNERABILITIES",
        "OTHER",
    ],
    typing.Any,
]
