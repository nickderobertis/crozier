

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IndexWebsiteResponse(UniversalBaseModel):
    job_id: str = pydantic.Field()
    """
    ID to track the indexing job status
    """

    base_url: str = pydantic.Field()
    """
    The base URL being indexed
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
