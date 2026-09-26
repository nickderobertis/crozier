

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_cert_response import TaxCloudCertResponse


class TaxCloudCertListResponse(UniversalBaseModel):
    items: typing.Optional[typing.List[TaxCloudCertResponse]] = pydantic.Field(default=None)
    """
    The exemption certificates on this page of results.
    """

    limit: int = pydantic.Field()
    """
    The maximum number of results per page that was applied.
    """

    next_cursor: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor",
            description="Opaque cursor to pass as 'cursor' on the next call to fetch the following page. Null when there are no further results.",
        ),
    ]
    """
    Opaque cursor to pass as 'cursor' on the next call to fetch the following page. Null when there are no further results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
