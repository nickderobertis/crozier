

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bulk_expunge_status import BulkExpungeStatus


class BulkExpungeContentsOut(UniversalBaseModel):
    results: typing.Dict[str, BulkExpungeStatus] = pydantic.Field()
    """
    Results of expunging (by ID)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
