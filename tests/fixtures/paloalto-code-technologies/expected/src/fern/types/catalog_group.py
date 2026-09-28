

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogGroup(enum.StrEnum):
    CODE = "Code"
    BUILD = "Build"
    DEPLOY = "Deploy"

    def visit(
        self,
        code: typing.Callable[[], T_Result],
        build: typing.Callable[[], T_Result],
        deploy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogGroup.CODE:
            return code()
        if self is CatalogGroup.BUILD:
            return build()
        if self is CatalogGroup.DEPLOY:
            return deploy()
