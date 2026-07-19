

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowSegmentPostGetUrlsItem(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    A URL to which a GET request can be made to directly retrieve the contents of the Media Object. Clients should include credentials if the provide URL is on the same origin as the API endpoint
    """

    label: str = pydantic.Field()
    """
    Label identifying this URL. Service implementations should reject any requests using labels that are already associated with Storage Backends. Service implementations should reject any requests containing multiple `get_urls` with the same `label`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
