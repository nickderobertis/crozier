

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .grep_gc_report import GrepGcReport


class ExtensionGcReports(UniversalBaseModel):
    """
    The reports from the extension collectors that one `gc` run ran, with one optional field for
    each extension.

    Each extension reports its collector under its own name here. A deployment that doesn't
    maintain an extension's state leaves that extension's field out, and a client ignores a name
    it doesn't know.
    """

    grep: typing.Optional[GrepGcReport] = pydantic.Field(default=None)
    """
    The counts from the grep index's collector, present when the deployment maintains a grep
    index.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
