

from __future__ import annotations

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .other_slurp_response_data_item import OtherSlurpResponseDataItem


class OtherSlurpResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[OtherSlurpResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/accounts/#appearance">Appearance</a>, <a href="/data-model/other/#function">Function</a>, <a href="/data-model/accounts/#monitor">Monitor</a>, <a href="/data-model/other/#parameter">Parameter</a> or <a href="/data-model/other/#slurp">Slurp</a> data. Corresponds to the <a href="/chifra/other/#chifra-slurp">chifra slurp</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(OtherSlurpResponse)
