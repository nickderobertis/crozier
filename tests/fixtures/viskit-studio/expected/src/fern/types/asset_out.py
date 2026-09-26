

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssetOut(UniversalBaseModel):
    download_url: str
    id: str
    image_id: str
    image_url: str
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    name: str
    output_kind: typing.Optional[str] = None
    source_image_ref: typing.Optional[str] = None
    source_job_id: typing.Optional[str] = None
    source_output_id: typing.Optional[str] = None
    template_ref: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
