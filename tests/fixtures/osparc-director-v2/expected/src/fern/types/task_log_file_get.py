

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskLogFileGet(UniversalBaseModel):
    task_id: str
    download_link: typing.Optional[str] = pydantic.Field(default=None)
    """
    Presigned link for log file or None if still not available
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
