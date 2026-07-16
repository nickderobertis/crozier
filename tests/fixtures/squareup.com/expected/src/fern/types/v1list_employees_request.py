

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1ListEmployeesRequest(UniversalBaseModel):
    """ """

    batch_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to retrieve the next set of results for your
    original query to the endpoint.
    """

    begin_created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.
    """

    begin_updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format
    """

    end_created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.
    """

    end_updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If provided, the endpoint returns only employee entities with the specified external_id.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    """

    order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order in which employees are listed in the response, based on their created_at field.      Default value: ASC
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
