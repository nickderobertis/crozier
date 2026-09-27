

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .integration_health_status import IntegrationHealthStatus


class IntegrationHealth(UniversalBaseModel):
    """
    Per-integration connection-liveness verdict computed synchronously by the verify endpoint. Distinct from the composite presence-health score.
    """

    platform: str
    external_id: typing_extensions.Annotated[str, FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")]
    status: IntegrationHealthStatus
    reason_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="reasonCode"),
        pydantic.Field(
            alias="reasonCode",
            description="Stable machine code resolved to human copy on the client (e.g. tg_not_admin, vk_wall_scope_missing, yandex_session_expired, ok, inconclusive).",
        ),
    ]
    """
    Stable machine code resolved to human copy on the client (e.g. tg_not_admin, vk_wall_scope_missing, yandex_session_expired, ok, inconclusive).
    """

    checked_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="checkedAt"), pydantic.Field(alias="checkedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
