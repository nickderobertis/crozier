

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_autocomplete_result import CoreAutocompleteResult
from .ocs_meta import OcsMeta


class CoreAutoCompleteGet200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: typing.List[CoreAutocompleteResult]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
