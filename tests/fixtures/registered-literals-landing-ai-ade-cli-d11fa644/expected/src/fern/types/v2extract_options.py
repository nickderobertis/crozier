

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2ExtractOptions(UniversalBaseModel):
    """
    Extraction options (``docs/extract-v2-proposal.md`` → Options).
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When ``true``, a schema containing fields the model cannot extract fails with a validation error — HTTP 422 on the sync route, or a failed job (``status: "failed"``) on the async ``/jobs`` route. When ``false`` (default), unsupported fields are skipped and extraction continues.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
