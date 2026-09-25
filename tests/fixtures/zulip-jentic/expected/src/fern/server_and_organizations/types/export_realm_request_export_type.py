

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ExportRealmRequestExportType(enum.StrEnum):
    """
    Whether the data export should be public, full with consent,
    or full without consent.

    - `public` = Public data only export.
    - `full_with_consent` = Public and private data export (with consent), which includes
      private data for users who have granted consent.
    - `full_without_consent` = All public and private data export, which includes private data for
      all users. This option requires the organization to have
      the `owner_full_content_access` feature enabled.

    If not specified, defaults to `public`.

    **Changes**: Zulip 12.0 (feature level 449) changed the type of
    this field from int to string with `1` being replaced by `public` and
    `2` being replaced by `full_with_consent`. The option `full_without_consent`
    was added for full exports without member consent.

    **Changes**: New in Zulip 10.0 (feature level 304). Previously,
    all export requests were public data exports.
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
        if self is ExportRealmRequestExportType.PUBLIC:
            return public()
        if self is ExportRealmRequestExportType.FULL_WITH_CONSENT:
            return full_with_consent()
        if self is ExportRealmRequestExportType.FULL_WITHOUT_CONSENT:
            return full_without_consent()
