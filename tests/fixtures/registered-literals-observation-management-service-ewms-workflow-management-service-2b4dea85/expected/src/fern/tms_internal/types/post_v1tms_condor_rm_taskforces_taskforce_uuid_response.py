

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostV1TmsCondorRmTaskforcesTaskforceUuidResponse(UniversalBaseModel):
    taskforce_uuid: str = pydantic.Field()
    """
    A unique identifier automatically generated for this taskforce.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
