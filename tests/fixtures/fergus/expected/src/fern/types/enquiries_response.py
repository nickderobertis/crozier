

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enquiry_with_job_ids import EnquiryWithJobIds
from .pagination import Pagination


class EnquiriesResponse(UniversalBaseModel):
    result: str
    data: typing.List[EnquiryWithJobIds]
    paging: typing.Optional[Pagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
