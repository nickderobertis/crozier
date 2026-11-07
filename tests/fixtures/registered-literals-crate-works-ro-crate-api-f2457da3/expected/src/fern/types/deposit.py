

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deposit_errors_item import DepositErrorsItem
from .deposit_state import DepositState
from .id import Id
from .staged_file import StagedFile


class Deposit(UniversalBaseModel):
    """
    A deposit session against an RO-Crate.

    A deposit is opened against a new RO-Crate (`POST /deposits`) or an existing one (`POST /ro-crate/{id}/deposits`), staged with a metadata document and files, then finalised. Deposits are single-use: once `complete` they are finished, and further changes open a new deposit.
    """

    deposit_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="depositId"),
        pydantic.Field(alias="depositId", description="Server-minted opaque identifier for this deposit."),
    ]
    """
    Server-minted opaque identifier for this deposit.
    """

    ro_crate_id: typing_extensions.Annotated[
        Id,
        FieldMetadata(alias="roCrateId"),
        pydantic.Field(
            alias="roCrateId",
            description="The RO-Crate this deposit targets. Once the deposit is `complete`, retrieve it via `GET /ro-crate/{id}` — its `entityIds` list is the authoritative answer to what the deposit materialised.",
        ),
    ]
    """
    The RO-Crate this deposit targets. Once the deposit is `complete`, retrieve it via `GET /ro-crate/{id}` — its `entityIds` list is the authoritative answer to what the deposit materialised.
    """

    state: DepositState = pydantic.Field()
    """
    The deposit's lifecycle state. `open` - accepting staging calls; `finalising` - a finalise is in progress and staging calls are rejected with 409; `complete` - the RO-Crate's new version is published (terminal); `aborted` - explicitly aborted or expired, staged content discarded (terminal). A failed finalise returns the deposit to `open` with the failure recorded in `errors`.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt",
            description="When the deposit was created. This is also the moment the carry-forward baseline is pinned for update deposits.",
        ),
    ] = None
    """
    When the deposit was created. This is also the moment the carry-forward baseline is pinned for update deposits.
    """

    files: typing.Optional[typing.List[StagedFile]] = pydantic.Field(default=None)
    """
    The files staged in this deposit, with per-file upload status. Status MAY be updated eagerly or lazily; finalise is the authoritative verification point.
    """

    errors: typing.Optional[typing.List[DepositErrorsItem]] = pydantic.Field(default=None)
    """
    The violations recorded when the most recent finalise failed and the deposit returned to `open`. Cleared when the next finalise is accepted; absent when there has been no failure.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
