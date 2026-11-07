

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WorkflowDocumentInput(UniversalBaseModel):
    """
    One declared document input in the ``inputs`` map.

    A caller supplies exactly one of ``document`` or ``document_url``:

    * ``document`` — name of a multipart form part carrying the raw bytes. The
      gateway stages those bytes internally before the workflow runs.
    * ``document_url`` — public URL (SSRF-validated at submit; fetched and staged
      by the gateway before the workflow starts).
    """

    document: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the multipart form part carrying the document bytes. The gateway resolves this to an internal ref before validation; it is not stored in the final request object.
    """

    document_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to fetch the document from. Must be a public http(s) URL; private/loopback IPs are rejected at submit time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
