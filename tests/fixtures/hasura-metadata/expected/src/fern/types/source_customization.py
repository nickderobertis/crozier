

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .naming_case import NamingCase
from .root_fields_customization import RootFieldsCustomization
from .source_type_customization import SourceTypeCustomization


class SourceCustomization(UniversalBaseModel):
    naming_convention: typing.Optional[NamingCase] = None
    root_fields: typing.Optional[RootFieldsCustomization] = None
    type_names: typing.Optional[SourceTypeCustomization] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
