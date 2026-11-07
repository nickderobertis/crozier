

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hash256 import Hash256
from .siacoin_origin_source import SiacoinOriginSource


class SiacoinOrigin(UniversalBaseModel):
    """
    Origin information for a siacoin output, analogous to txnid:vout in Bitcoin.
    """

    source: SiacoinOriginSource = pydantic.Field()
    """
    The source type of the siacoin output.
    """

    id: Hash256 = pydantic.Field()
    """
    The ID of the source (transaction ID, block ID, or contract ID).
    """

    index: int = pydantic.Field()
    """
    The index of the output within the source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
