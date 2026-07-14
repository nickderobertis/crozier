

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatchPresignMultipartPartsResponse(UniversalBaseModel):
    presigned_urls: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    The presigned URLs for each part number, which has
    the part numbers as keys.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
