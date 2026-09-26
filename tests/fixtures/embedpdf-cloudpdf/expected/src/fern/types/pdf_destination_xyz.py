

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_destination_xyz_page import PdfDestinationXyzPage


class PdfDestinationXyz(UniversalBaseModel):
    page: PdfDestinationXyzPage
    left: typing.Optional[float] = None
    top: typing.Optional[float] = None
    zoom: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
