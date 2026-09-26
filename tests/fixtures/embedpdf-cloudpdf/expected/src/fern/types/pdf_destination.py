

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pdf_destination_fit_b_page import PdfDestinationFitBPage
from .pdf_destination_fit_bh_page import PdfDestinationFitBhPage
from .pdf_destination_fit_bv_page import PdfDestinationFitBvPage
from .pdf_destination_fit_h_page import PdfDestinationFitHPage
from .pdf_destination_fit_page import PdfDestinationFitPage
from .pdf_destination_fit_r_page import PdfDestinationFitRPage
from .pdf_destination_fit_v_page import PdfDestinationFitVPage
from .pdf_destination_xyz_page import PdfDestinationXyzPage


class PdfDestination_Xyz(UniversalBaseModel):
    kind: typing.Literal["xyz"] = "xyz"
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


class PdfDestination_Fit(UniversalBaseModel):
    kind: typing.Literal["fit"] = "fit"
    page: PdfDestinationFitPage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfDestination_FitH(UniversalBaseModel):
    kind: typing.Literal["fitH"] = "fitH"
    page: PdfDestinationFitHPage
    top: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfDestination_FitV(UniversalBaseModel):
    kind: typing.Literal["fitV"] = "fitV"
    page: PdfDestinationFitVPage
    left: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfDestination_FitR(UniversalBaseModel):
    kind: typing.Literal["fitR"] = "fitR"
    page: PdfDestinationFitRPage
    left: float
    bottom: float
    right: float
    top: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfDestination_FitB(UniversalBaseModel):
    kind: typing.Literal["fitB"] = "fitB"
    page: PdfDestinationFitBPage

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfDestination_FitBh(UniversalBaseModel):
    kind: typing.Literal["fitBH"] = "fitBH"
    page: PdfDestinationFitBhPage
    top: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PdfDestination_FitBv(UniversalBaseModel):
    kind: typing.Literal["fitBV"] = "fitBV"
    page: PdfDestinationFitBvPage
    left: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PdfDestination = typing_extensions.Annotated[
    typing.Union[
        PdfDestination_Xyz,
        PdfDestination_Fit,
        PdfDestination_FitH,
        PdfDestination_FitV,
        PdfDestination_FitR,
        PdfDestination_FitB,
        PdfDestination_FitBh,
        PdfDestination_FitBv,
    ],
    pydantic.Field(discriminator="kind"),
]
