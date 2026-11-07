

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSettingsResponse(UniversalBaseModel):
    ask_ai_enabled: bool = pydantic.Field()
    """
    Whether Ask AI is enabled (requires one of docs or slack to be enabled as well as the content to be indexed)
    """

    job_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Active job ID if reindexing is in progress
    """

    docs_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether Ask AI is enabled for docs
    """

    slack_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether Ask AI is enabled for slack
    """

    decompose_queries: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether query decomposition is enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
