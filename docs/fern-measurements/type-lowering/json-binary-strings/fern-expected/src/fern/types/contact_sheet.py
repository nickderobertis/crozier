

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContactSheet(UniversalBaseModel):
    master: bytes
    frames: typing.Optional[typing.List[str]] = None
    layers: typing.Optional[typing.Dict[str, str]] = None
    overlay: typing.Optional[bytes] = None
    backing: typing.Optional[bytes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
