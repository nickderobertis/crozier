

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.site import Site
from ...types.site_outline import SiteOutline


class RecordSitesRequest_Site(UniversalBaseModel):
    type: typing.Literal["Site"] = "Site"
    name: str
    outline: typing.Optional[SiteOutline] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class RecordSitesRequest_SiteBatch(UniversalBaseModel):
    type: typing.Literal["SiteBatch"] = "SiteBatch"
    extent: typing.Optional[typing.List[typing.Any]] = None
    sites: typing.List[Site]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


RecordSitesRequest = typing_extensions.Annotated[
    typing.Union[RecordSitesRequest_Site, RecordSitesRequest_SiteBatch], pydantic.Field(discriminator="type")
]
