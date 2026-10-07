

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EsmSpec(UniversalBaseModel):
    """
    Where the frontend imports a widget's ESM from, and which version.

        Specs travel only on kernel-authored notifications, never in model
        state: state is client-writable and echoed to peers, so executing
        code from it would let one client run code on another.

        Attributes:
            url: URL to import the ESM from. A virtual file for inline
                source; an external URL when `_esm` is itself a URL.
            hash: Hash of the `_esm` string. Keys the frontend module cache
                and signals code changes (hot reload).
    """

    hash: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
