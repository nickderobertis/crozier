

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostUpdatesUploadVariantRequestVariant(enum.StrEnum):
    JAR = "JAR"
    EXE_WINDOWS_X8664 = "EXE_WINDOWS_X86_64"
    EXE_WINDOWS_X86 = "EXE_WINDOWS_X86"
    EXE_WINDOWS_ARM64 = "EXE_WINDOWS_ARM64"
    LINUX_X86 = "LINUX_X86"
    LINUX_X8664 = "LINUX_X86_64"
    LINUX_ARM64 = "LINUX_ARM64"
    LINUX_ARM32 = "LINUX_ARM32"
    MACOS_X8664 = "MACOS_X86_64"
    MACOS_ARM64 = "MACOS_ARM64"

    def visit(
        self,
        jar: typing.Callable[[], T_Result],
        exe_windows_x8664: typing.Callable[[], T_Result],
        exe_windows_x86: typing.Callable[[], T_Result],
        exe_windows_arm64: typing.Callable[[], T_Result],
        linux_x86: typing.Callable[[], T_Result],
        linux_x8664: typing.Callable[[], T_Result],
        linux_arm64: typing.Callable[[], T_Result],
        linux_arm32: typing.Callable[[], T_Result],
        macos_x8664: typing.Callable[[], T_Result],
        macos_arm64: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostUpdatesUploadVariantRequestVariant.JAR:
            return jar()
        if self is PostUpdatesUploadVariantRequestVariant.EXE_WINDOWS_X8664:
            return exe_windows_x8664()
        if self is PostUpdatesUploadVariantRequestVariant.EXE_WINDOWS_X86:
            return exe_windows_x86()
        if self is PostUpdatesUploadVariantRequestVariant.EXE_WINDOWS_ARM64:
            return exe_windows_arm64()
        if self is PostUpdatesUploadVariantRequestVariant.LINUX_X86:
            return linux_x86()
        if self is PostUpdatesUploadVariantRequestVariant.LINUX_X8664:
            return linux_x8664()
        if self is PostUpdatesUploadVariantRequestVariant.LINUX_ARM64:
            return linux_arm64()
        if self is PostUpdatesUploadVariantRequestVariant.LINUX_ARM32:
            return linux_arm32()
        if self is PostUpdatesUploadVariantRequestVariant.MACOS_X8664:
            return macos_x8664()
        if self is PostUpdatesUploadVariantRequestVariant.MACOS_ARM64:
            return macos_arm64()
