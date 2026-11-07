

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_element_options import BaseElementOptions
from .figure_options import FigureOptions
from .table_options import TableOptions


class BlocksOptions(UniversalBaseModel):
    text: typing.Optional[BaseElementOptions] = None
    table: typing.Optional[TableOptions] = None
    figure: typing.Optional[FigureOptions] = None
    marginalia: typing.Optional[BaseElementOptions] = None
    attestation: typing.Optional[BaseElementOptions] = None
    logo: typing.Optional[BaseElementOptions] = None
    scan_code: typing.Optional[BaseElementOptions] = None
    card: typing.Optional[BaseElementOptions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
