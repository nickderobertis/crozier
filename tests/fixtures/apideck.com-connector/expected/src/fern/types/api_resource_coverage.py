

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_resource_coverage_coverage_item import ApiResourceCoverageCoverageItem
from .resource_status import ResourceStatus


class ApiResourceCoverage(UniversalBaseModel):
    coverage: typing.Optional[typing.List[ApiResourceCoverageCoverageItem]] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the resource, typically a lowercased version of name.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the resource (plural)
    """

    status: typing.Optional[ResourceStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ApiResourceCoverage)
