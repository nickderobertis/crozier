

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ListOrdersRequest(UniversalBaseModel):
    """ """

    batch_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to retrieve the next set of results for your
    original query to the endpoint.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of payments to return in a single response. This value cannot exceed 200.
    """

    order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which payments are listed in the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
