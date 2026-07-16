

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListDeviceCodesRequest(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor returned by a previous call to this endpoint.
    Provide this to retrieve the next set of results for your original query.
    
    See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If specified, only returns DeviceCodes of the specified location.
    Returns DeviceCodes of all locations if empty.
    """

    product_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    If specified, only returns DeviceCodes targeting the specified product type.
    Returns DeviceCodes of all product types if empty.
    """

    status: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    If specified, returns DeviceCodes with the specified statuses.
    Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
