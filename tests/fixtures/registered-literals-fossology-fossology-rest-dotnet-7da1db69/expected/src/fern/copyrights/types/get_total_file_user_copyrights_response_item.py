

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetTotalFileUserCopyrightsResponseItem(UniversalBaseModel):
    total_copyrights: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total Number of user copyright findings for the uploadtree
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
