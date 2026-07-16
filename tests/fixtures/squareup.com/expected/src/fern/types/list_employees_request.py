

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListEmployeesRequest(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The token required to retrieve the specified page of results.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of employees to be returned on each page.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies the EmployeeStatus to filter the employee by.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
