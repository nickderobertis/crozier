

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chaindata_when_response_data_item import ChaindataWhenResponseDataItem


class ChaindataWhenResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[ChaindataWhenResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/other/#count">Count</a>, <a href="/data-model/other/#message">Message</a>, <a href="/data-model/chaindata/#namedblock">NamedBlock</a> or <a href="/data-model/chaindata/#timestamp">Timestamp</a> data. Corresponds to the <a href="/chifra/chaindata/#chifra-when">chifra when</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
