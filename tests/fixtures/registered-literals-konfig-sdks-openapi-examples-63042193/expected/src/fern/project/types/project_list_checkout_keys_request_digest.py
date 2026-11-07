

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectListCheckoutKeysRequestDigest(enum.StrEnum):
    SHA256 = "sha256"
    MD5 = "md5"

    def visit(self, sha256: typing.Callable[[], T_Result], md5: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectListCheckoutKeysRequestDigest.SHA256:
            return sha256()
        if self is ProjectListCheckoutKeysRequestDigest.MD5:
            return md5()
