

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contact_sheet import ContactSheet


class Print(UniversalBaseModel):
    image: str
    thumbnail: typing.Optional[bytes] = None
    proofs: typing.Optional[typing.List[str]] = None
    checksum: typing.Optional[str] = None
    caption: typing.Optional[str] = None
    sheet: typing.Optional[ContactSheet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
