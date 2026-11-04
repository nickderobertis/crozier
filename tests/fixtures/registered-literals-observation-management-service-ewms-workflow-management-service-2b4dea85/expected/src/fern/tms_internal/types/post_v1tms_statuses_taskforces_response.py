

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1tms_statuses_taskforces_response_results_item import PostV1TmsStatusesTaskforcesResponseResultsItem


class PostV1TmsStatusesTaskforcesResponse(UniversalBaseModel):
    results: typing.List[PostV1TmsStatusesTaskforcesResponseResultsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
