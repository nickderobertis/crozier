

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DocumentsImportFromRequestSourceUrl(UniversalBaseModel):
    """
    The caller supplies the authority: a presigned S3/GCS/Azure/R2/MinIO GET, or any HTTPS endpoint the deployment import policy allows. The URL is a capability — treat it as a secret. CloudPDF never echoes its query string back in errors, logs, or stored failure reasons.
    """

    url: str = pydantic.Field()
    """
    The URL to fetch. Must be allowed by the deployment import policy (scheme, network range, size) and must declare a length.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
