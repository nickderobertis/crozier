

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .data_element_base import DataElementBase
from .multi_language_value import MultiLanguageValue


class MultiLanguageDataElement(DataElementBase):
    """
    Language-tagged values (EN 18223 clause 4.1.2.8).
    """

    value: typing.Optional[typing.List[MultiLanguageValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
