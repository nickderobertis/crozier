

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .conditions import Conditions
from .license_types import LicenseTypes
from .limitations import Limitations
from .permissions import Permissions


class License(UniversalBaseModel):
    id: str
    name: str
    url: typing.Optional[str] = None
    type: typing.Optional[LicenseTypes] = None
    conditions: typing.Optional[typing.List[Conditions]] = None
    permissions: typing.Optional[typing.List[Permissions]] = None
    limitations: typing.Optional[typing.List[Limitations]] = None
    compatibility: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
