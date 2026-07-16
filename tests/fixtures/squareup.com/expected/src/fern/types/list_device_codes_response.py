

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_code import DeviceCode
from .error import Error


class ListDeviceCodesResponse(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to retrieve the next set of results for your
    original query to the endpoint. This value is present only if the request
    succeeded and additional results are available.
    
    See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    """

    device_codes: typing.Optional[typing.List[DeviceCode]] = pydantic.Field(default=None)
    """
    The queried DeviceCode.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
