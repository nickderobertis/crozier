

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_init_response_data_item import AdminInitResponseDataItem


class AdminInitResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[AdminInitResponseDataItem]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/admin/#chunkrecord">ChunkRecord</a> or <a href="/data-model/admin/#manifest">Manifest</a> data. Corresponds to the <a href="/chifra/admin/#chifra-init">chifra init</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
