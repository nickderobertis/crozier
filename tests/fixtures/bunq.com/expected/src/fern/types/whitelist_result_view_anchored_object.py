

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .draft_payment import DraftPayment
from .request_response import RequestResponse


class WhitelistResultViewAnchoredObject(UniversalBaseModel):
    draft_payment: typing_extensions.Annotated[
        typing.Optional[DraftPayment],
        FieldMetadata(alias="draftPayment"),
        pydantic.Field(alias="draftPayment", description="The DraftPayment object"),
    ] = None
    """
    The DraftPayment object
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the whitelist entry.
    """

    request_response: typing_extensions.Annotated[
        typing.Optional[RequestResponse],
        FieldMetadata(alias="requestResponse"),
        pydantic.Field(alias="requestResponse", description="The RequestResponse object"),
    ] = None
    """
    The RequestResponse object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WhitelistResultViewAnchoredObject)
