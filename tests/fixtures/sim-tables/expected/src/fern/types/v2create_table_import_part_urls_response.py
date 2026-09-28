

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2part_urls_data import V2PartUrlsData


class V2CreateTableImportPartUrlsResponse(UniversalBaseModel):
    """
    Signed URLs and required headers for each requested upload part.
    """

    data: V2PartUrlsData = pydantic.Field()
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
