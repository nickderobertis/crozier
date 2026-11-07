

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Receipt(UniversalBaseModel):
    """
    The receipt associated with the expense.
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the receipt.
    """

    download_uris: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    [Presigned S3 link](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)(s) to download file(s) of the receipt. Link(s) expire in 15 minutes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
