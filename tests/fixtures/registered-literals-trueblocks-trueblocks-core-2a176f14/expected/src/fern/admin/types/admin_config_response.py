

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.chain import Chain


class AdminConfigResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[Chain]] = pydantic.Field(default=None)
    """
    Produces <a href="/data-model/admin/#chain">Chain</a> data. Corresponds to the <a href="/chifra/admin/#chifra-config">chifra config</a> command line.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
