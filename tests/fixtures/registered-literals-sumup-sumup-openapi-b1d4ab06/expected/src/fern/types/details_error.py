

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .details_error_failed_constraints_item import DetailsErrorFailedConstraintsItem


class DetailsError(UniversalBaseModel):
    """
    Details of a request validation error.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short title of the error.
    """

    details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Details of the error.
    """

    status: typing.Optional[float] = pydantic.Field(default=None)
    """
    HTTP status code for the error.
    """

    failed_constraints: typing.Optional[typing.List[DetailsErrorFailedConstraintsItem]] = pydantic.Field(default=None)
    """
    List of violated validation constraints.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
