

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfResponseComponentType(enum.StrEnum):
    """
    shows component type
    """

    PURL = "purl"
    MAVEN = "maven"
    NUGET = "nuget"
    NPM = "npm"
    PYPI = "pypi"
    PACKAGE_URL = "package-url"

    def visit(
        self,
        purl: typing.Callable[[], T_Result],
        maven: typing.Callable[[], T_Result],
        nuget: typing.Callable[[], T_Result],
        npm: typing.Callable[[], T_Result],
        pypi: typing.Callable[[], T_Result],
        package_url: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfResponseComponentType.PURL:
            return purl()
        if self is ConfResponseComponentType.MAVEN:
            return maven()
        if self is ConfResponseComponentType.NUGET:
            return nuget()
        if self is ConfResponseComponentType.NPM:
            return npm()
        if self is ConfResponseComponentType.PYPI:
            return pypi()
        if self is ConfResponseComponentType.PACKAGE_URL:
            return package_url()
