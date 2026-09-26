

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_destination_fit_h_page import PdfDestinationFitHPage


class PdfDestinationFitH(UniversalBaseModel):
    page: PdfDestinationFitHPage
    top: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
