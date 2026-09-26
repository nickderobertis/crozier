

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RealmExportExportType(enum.StrEnum):
    """
    Whether the data export is public, full with consent, or full without consent.

    - `public` = Public data export.
    - `full_with_consent` = Public and private data export (with consent), which includes private data
      for users who have granted consent.
    - `full_without_consent` = All public and private data, which includes private data for all users.

    **Changes**: Zulip 12.0 (feature level 449) changed the type of
    this field from int to string with `1` being replaced by `public` and
    `2` being replaced by `full_with_consent`. The option `full_without_consent`
    was added for full exports without member consent.

    **Changes**: New in Zulip 10.0 (feature level 304). Previously,
    the export type was not included in these objects because only
    public data exports could be created or listed via the API or UI.
    """

    PUBLIC = "public"
    FULL_WITH_CONSENT = "full_with_consent"
    FULL_WITHOUT_CONSENT = "full_without_consent"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        full_with_consent: typing.Callable[[], T_Result],
        full_without_consent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RealmExportExportType.PUBLIC:
            return public()
        if self is RealmExportExportType.FULL_WITH_CONSENT:
            return full_with_consent()
        if self is RealmExportExportType.FULL_WITHOUT_CONSENT:
            return full_without_consent()
