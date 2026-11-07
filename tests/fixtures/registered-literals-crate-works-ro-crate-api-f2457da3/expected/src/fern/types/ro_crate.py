

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .id import Id
from .ro_crate_access import RoCrateAccess


class RoCrate(UniversalBaseModel):
    """
    An RO-Crate is the unit of deposit: a metadata document plus all the files it references, stored as deposited.

    Catalog entities are materialised from RO-Crates by implementation-specific rules — one RO-Crate may yield one entity or many, and several RO-Crates may contribute to a single merged entity. The deposited metadata document (`GET /ro-crate/{id}/metadata`) is the single source of truth for the RO-Crate's content inventory; the RO-Crate carries no file list of its own.
    """

    id: Id = pydantic.Field()
    """
    The RO-Crate's ID.
    """

    entity_ids: typing_extensions.Annotated[
        typing.List[Id],
        FieldMetadata(alias="entityIds"),
        pydantic.Field(
            alias="entityIds",
            description="The entities materialised from this RO-Crate's current version — the inverse of the entity's `roCrateIds`. Can change when later deposits (of this or other RO-Crates) alter the materialisation.",
        ),
    ]
    """
    The entities materialised from this RO-Crate's current version — the inverse of the entity's `roCrateIds`. Can change when later deposits (of this or other RO-Crates) alter the materialisation.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt", description="When the RO-Crate was first created (its first successful finalise)."
        ),
    ]
    """
    When the RO-Crate was first created (its first successful finalise).
    """

    last_deposited_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastDepositedAt"),
        pydantic.Field(
            alias="lastDepositedAt",
            description="When the RO-Crate's current version was published (its most recent successful finalise).",
        ),
    ]
    """
    When the RO-Crate's current version was published (its most recent successful finalise).
    """

    access: RoCrateAccess = pydantic.Field()
    """
    Access information for this RO-Crate. `metadata` governs this resource; `content` governs the deposited metadata document and file retrieval.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
