

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .job_properties import JobProperties
from .resource import Resource


class JobResource(Resource):
    """
    Job Resource.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the object.
    """

    properties: JobProperties = pydantic.Field()
    """
    Properties of a job.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
