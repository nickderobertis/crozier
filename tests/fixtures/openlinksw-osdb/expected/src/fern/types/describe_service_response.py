

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .describe_service_response_status import DescribeServiceResponseStatus
from .service_description import ServiceDescription


class DescribeServiceResponse(UniversalBaseModel):
    api: str = pydantic.Field()
    """
    The path of the REST API method
    """

    method: str = pydantic.Field()
    """
    The name of the REST API method
    """

    response: ServiceDescription
    status: DescribeServiceResponseStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
