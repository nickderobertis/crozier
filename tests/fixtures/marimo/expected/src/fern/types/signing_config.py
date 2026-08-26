

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SigningConfig(UniversalBaseModel):
    """
    Cache-signing trust and identity.

        `trusted_signers` maps a key fingerprint (`"SHA256:<base64>"`) to an
        advisory label. Trusting a key allows arbitrary code execution from its
        holder on this machine — a cache restore is `pickle.loads` — so there is no
        lesser cache-only grant. `private_key_path` is this machine's signing
        identity; it is never serialized to the frontend.
    """

    private_key_path: typing.Optional[str] = None
    trusted_signers: typing.Optional[typing.Dict[str, str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
