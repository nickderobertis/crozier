

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleCloudServicebrokerV1Alpha1DashboardClient(UniversalBaseModel):
    """
    Message containing information required to activate Dashboard SSO feature.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the Oauth client that the dashboard will use.
    """

    redirect_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    A URI for the service dashboard.
    Validated by the OAuth token server when the dashboard requests a token.
    """

    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    A secret for the dashboard client.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
