

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobQueueDownload(UniversalBaseModel):
    """
    Report download information
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Text for download link
    """

    link: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to download the report
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
