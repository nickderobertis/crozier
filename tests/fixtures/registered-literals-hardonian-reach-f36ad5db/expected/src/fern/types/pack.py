

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pack_reproducibility import PackReproducibility


class Pack(UniversalBaseModel):
    name: str
    repo: str
    spec_version: str
    signature: typing.Optional[str] = None
    reproducibility: typing.Optional[PackReproducibility] = None
    verified: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
