

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ExecBodyOsdbOutputType(enum.StrEnum):
    """
    An OSDB-specific parameter controlling the action output type. If omitted, the native action output is returned.
    """

    URL_ONLY = "url_only"
    GENERATE_RDF = "generate_rdf"
    DISPLAY_RDF = "display_rdf"

    def visit(
        self,
        url_only: typing.Callable[[], T_Result],
        generate_rdf: typing.Callable[[], T_Result],
        display_rdf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExecBodyOsdbOutputType.URL_ONLY:
            return url_only()
        if self is ExecBodyOsdbOutputType.GENERATE_RDF:
            return generate_rdf()
        if self is ExecBodyOsdbOutputType.DISPLAY_RDF:
            return display_rdf()
