

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AdminChunksRequestMode(enum.StrEnum):
    MANIFEST = "manifest"
    INDEX = "index"
    BLOOMS = "blooms"
    PINS = "pins"
    ADDRESSES = "addresses"
    APPEARANCES = "appearances"
    STATS = "stats"

    def visit(
        self,
        manifest: typing.Callable[[], T_Result],
        index: typing.Callable[[], T_Result],
        blooms: typing.Callable[[], T_Result],
        pins: typing.Callable[[], T_Result],
        addresses: typing.Callable[[], T_Result],
        appearances: typing.Callable[[], T_Result],
        stats: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdminChunksRequestMode.MANIFEST:
            return manifest()
        if self is AdminChunksRequestMode.INDEX:
            return index()
        if self is AdminChunksRequestMode.BLOOMS:
            return blooms()
        if self is AdminChunksRequestMode.PINS:
            return pins()
        if self is AdminChunksRequestMode.ADDRESSES:
            return addresses()
        if self is AdminChunksRequestMode.APPEARANCES:
            return appearances()
        if self is AdminChunksRequestMode.STATS:
            return stats()
