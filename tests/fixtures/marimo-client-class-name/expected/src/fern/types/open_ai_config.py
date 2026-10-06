

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OpenAiConfig(UniversalBaseModel):
    """
    Configuration options for OpenAI or OpenAI-compatible services.

        **Keys.**

        - `api_key`: the OpenAI API key
        - `base_url`: the base URL for the API
        - `project`: the project ID for the OpenAI API
        - `ssl_verify` : Boolean argument for httpx passed to open ai client. httpx defaults to true, but some use cases to let users override to False in some testing scenarios
        - `ca_bundle_path`: custom ca bundle to be used for verifying SSL certificates. Used to create custom SSL context for httpx client
        - `client_pem` : custom path of a client .pem cert used for verifying identity of client server
        - `extra_headers`: extra headers to be passed to the OpenAI client
    """

    api_key: typing.Optional[str] = None
    base_url: typing.Optional[str] = None
    ca_bundle_path: typing.Optional[str] = None
    client_pem: typing.Optional[str] = None
    extra_headers: typing.Optional[typing.Dict[str, str]] = None
    model: typing.Optional[str] = None
    project: typing.Optional[str] = None
    ssl_verify: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
