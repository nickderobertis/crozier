

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .analysis_archive_add_result_status import AnalysisArchiveAddResultStatus


class AnalysisArchiveAddResult(UniversalBaseModel):
    """
    The result of adding a single digest to the archive
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Details on the status, e.g. the error message
    """

    digest: typing.Optional[str] = pydantic.Field(default=None)
    """
    The image digest requested to be added
    """

    status: typing.Optional[AnalysisArchiveAddResultStatus] = pydantic.Field(default=None)
    """
    The status of the archive add operation. Typically either 'archived' or 'error'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
