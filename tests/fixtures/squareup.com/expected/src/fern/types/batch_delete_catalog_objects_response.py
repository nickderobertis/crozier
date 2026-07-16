

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error


class BatchDeleteCatalogObjectsResponse(UniversalBaseModel):
    """ """

    deleted_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The database [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) of this deletion in RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z".
    """

    deleted_object_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of all CatalogObjects deleted by this request.
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
