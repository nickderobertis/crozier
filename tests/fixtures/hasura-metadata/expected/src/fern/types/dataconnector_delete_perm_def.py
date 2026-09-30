

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataconnector_del_perm import DataconnectorDelPerm


class DataconnectorDeletePermDef(UniversalBaseModel):
    comment: typing.Optional[str] = None
    permission: DataconnectorDelPerm
    role: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
