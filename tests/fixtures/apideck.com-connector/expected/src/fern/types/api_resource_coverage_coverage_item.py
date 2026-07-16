

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .pagination_coverage import PaginationCoverage


class ApiResourceCoverageCoverageItem(UniversalBaseModel):
    downstream_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the resource in the Connector's API (downstream)
    """

    downstream_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the resource in the Connector's API (downstream)
    """

    pagination: typing.Optional[PaginationCoverage] = None
    pagination_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if pagination (cursor and limit parameters) is supported on the list endpoint of the resource.
    """

    supported_fields: typing.Optional[typing.List["SupportedProperty"]] = pydantic.Field(default=None)
    """
    Supported fields on the detail endpoint.
    """

    supported_filters: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Supported filters on the list endpoint of the resource.
    """

    supported_list_fields: typing.Optional[typing.List["SupportedProperty"]] = pydantic.Field(default=None)
    """
    Supported fields on the list endpoint.
    """

    supported_operations: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of supported operations on the resource.
    """

    supported_sort_by: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Supported sorting properties on the list endpoint of the resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .supported_property import SupportedProperty
from .supported_property_child_properties_item import SupportedPropertyChildPropertiesItem

update_forward_refs(
    ApiResourceCoverageCoverageItem,
    SupportedProperty=SupportedProperty,
    SupportedPropertyChildPropertiesItem=SupportedPropertyChildPropertiesItem,
)
