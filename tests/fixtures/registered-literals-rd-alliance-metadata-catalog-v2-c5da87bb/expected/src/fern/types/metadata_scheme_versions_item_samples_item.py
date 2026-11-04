

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetadataSchemeVersionsItemSamplesItem(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the sample record. For samples hosted by the MSC, the URL should be specified in relative form.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the title element from the sample record, or an equivalent short summary of what the sample record describes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
