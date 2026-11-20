

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_glaze_firings_response_batch import ListGlazeFiringsResponseBatch
from .list_glaze_firings_response_firings_value import ListGlazeFiringsResponseFiringsValue


class ListGlazeFiringsResponse(UniversalBaseModel):
    batch: ListGlazeFiringsResponseBatch
    firings: typing.Dict[str, typing.Optional[ListGlazeFiringsResponseFiringsValue]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
