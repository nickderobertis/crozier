

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ArtifactType(enum.StrEnum):
    """
    Specifies the type of external reference.
    """

    ATTESTATION = "ATTESTATION"
    BOM = "BOM"
    BUILD_META = "BUILD_META"
    CERTIFICATION = "CERTIFICATION"
    FORMULATION = "FORMULATION"
    LICENSE = "LICENSE"
    RELEASE_NOTES = "RELEASE_NOTES"
    SECURITY_TXT = "SECURITY_TXT"
    THREAT_MODEL = "THREAT_MODEL"
    VULNERABILITIES = "VULNERABILITIES"
    OTHER = "OTHER"

    def visit(
        self,
        attestation: typing.Callable[[], T_Result],
        bom: typing.Callable[[], T_Result],
        build_meta: typing.Callable[[], T_Result],
        certification: typing.Callable[[], T_Result],
        formulation: typing.Callable[[], T_Result],
        license: typing.Callable[[], T_Result],
        release_notes: typing.Callable[[], T_Result],
        security_txt: typing.Callable[[], T_Result],
        threat_model: typing.Callable[[], T_Result],
        vulnerabilities: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ArtifactType.ATTESTATION:
            return attestation()
        if self is ArtifactType.BOM:
            return bom()
        if self is ArtifactType.BUILD_META:
            return build_meta()
        if self is ArtifactType.CERTIFICATION:
            return certification()
        if self is ArtifactType.FORMULATION:
            return formulation()
        if self is ArtifactType.LICENSE:
            return license()
        if self is ArtifactType.RELEASE_NOTES:
            return release_notes()
        if self is ArtifactType.SECURITY_TXT:
            return security_txt()
        if self is ArtifactType.THREAT_MODEL:
            return threat_model()
        if self is ArtifactType.VULNERABILITIES:
            return vulnerabilities()
        if self is ArtifactType.OTHER:
            return other()
