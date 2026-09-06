

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdatePageSettingsRequestSeo(UniversalBaseModel):
    """
    SEO-related fields for the Page
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Page title shown in search engine results
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Page description shown in search engine results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
