

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_record_response_annotated import GetRecordResponseAnnotated
from .get_record_response_closed import GetRecordResponseClosed
from .get_record_response_fixed import GetRecordResponseFixed
from .get_record_response_open import GetRecordResponseOpen


class GetRecordResponse(UniversalBaseModel):
    annotated: typing.Optional[GetRecordResponseAnnotated] = pydantic.Field(default=None)
    """
    annotated
    """

    fixed: typing.Optional[GetRecordResponseFixed] = pydantic.Field(default=None)
    """
    annotated
    """

    closed: typing.Optional[GetRecordResponseClosed] = None
    open: typing.Optional[GetRecordResponseOpen] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
