

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreateArtifactRequestXRegistryHashAlgorithm(str, enum.Enum):
    SHA256 = "SHA256"
    MD5 = "MD5"

    def visit(self, sha256: typing.Callable[[], T_Result], md5: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateArtifactRequestXRegistryHashAlgorithm.SHA256:
            return sha256()
        if self is CreateArtifactRequestXRegistryHashAlgorithm.MD5:
            return md5()
