

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetCloudFrontOriginAccessIdentityConfigRequest(UniversalBaseModel):
    """
    The origin access identity's configuration information. For more information, see <a>CloudFrontOriginAccessIdentityConfigComplexType</a>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
