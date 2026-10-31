

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset_kind import AssetKind


class DocumentAsset(UniversalBaseModel):
    id: str
    kind: AssetKind
    uri: typing.Optional[str] = None
    data_base64: typing.Optional[str] = None
    mime_type: typing.Optional[str] = None
    page_number: typing.Optional[int] = None
    width: typing.Optional[float] = None
    height: typing.Optional[float] = None
    sha256: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
