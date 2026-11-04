

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .crtdl import Crtdl
from .upgrade_issue import UpgradeIssue


class UpgradeWrapper(UniversalBaseModel):
    crtdl: typing.Optional[Crtdl] = None
    annotations: typing.Optional[typing.List[UpgradeIssue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
