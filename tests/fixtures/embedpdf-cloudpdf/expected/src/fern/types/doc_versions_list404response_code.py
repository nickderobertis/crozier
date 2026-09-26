

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsList404ResponseCode(enum.StrEnum):
    UNKNOWN = "Unknown"
    INVALID_ARG = "InvalidArg"
    DOC_NOT_OPEN = "DocNotOpen"
    DOC_OPEN_FAILED = "DocOpenFailed"
    DOC_PASSWORD_REQUIRED = "DocPasswordRequired"
    DOC_PASSWORD_INCORRECT = "DocPasswordIncorrect"
    SHARE_PASSWORD_REQUIRED = "SharePasswordRequired"
    ABORTED = "Aborted"
    NETWORK = "Network"
    UNAUTHENTICATED = "Unauthenticated"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    WIRE_FORMAT = "WireFormat"
    RUNTIME_UNAVAILABLE = "RuntimeUnavailable"
    INVALID_REFERENCE = "InvalidReference"
    WEAK_ANNOTATION_SESSION_CONFLICT = "WeakAnnotationSessionConflict"
    LAYER_VERSION_CONFLICT = "LayerVersionConflict"
    NOT_IMPLEMENTED = "NotImplemented"
    MALFORMED_PDF = "MalformedPdf"
    SIGNING_PENDING = "SigningPending"
    SIGNING_EXPIRED = "SigningExpired"
    SIGNING_VERSION_MISMATCH = "SigningVersionMismatch"
    SIGNATURE_REFUSED = "SignatureRefused"
    PROTECTED_DOCUMENT = "ProtectedDocument"
    STALE_BASE = "StaleBase"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        invalid_arg: typing.Callable[[], T_Result],
        doc_not_open: typing.Callable[[], T_Result],
        doc_open_failed: typing.Callable[[], T_Result],
        doc_password_required: typing.Callable[[], T_Result],
        doc_password_incorrect: typing.Callable[[], T_Result],
        share_password_required: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        unauthenticated: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        wire_format: typing.Callable[[], T_Result],
        runtime_unavailable: typing.Callable[[], T_Result],
        invalid_reference: typing.Callable[[], T_Result],
        weak_annotation_session_conflict: typing.Callable[[], T_Result],
        layer_version_conflict: typing.Callable[[], T_Result],
        not_implemented: typing.Callable[[], T_Result],
        malformed_pdf: typing.Callable[[], T_Result],
        signing_pending: typing.Callable[[], T_Result],
        signing_expired: typing.Callable[[], T_Result],
        signing_version_mismatch: typing.Callable[[], T_Result],
        signature_refused: typing.Callable[[], T_Result],
        protected_document: typing.Callable[[], T_Result],
        stale_base: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsList404ResponseCode.UNKNOWN:
            return unknown()
        if self is DocVersionsList404ResponseCode.INVALID_ARG:
            return invalid_arg()
        if self is DocVersionsList404ResponseCode.DOC_NOT_OPEN:
            return doc_not_open()
        if self is DocVersionsList404ResponseCode.DOC_OPEN_FAILED:
            return doc_open_failed()
        if self is DocVersionsList404ResponseCode.DOC_PASSWORD_REQUIRED:
            return doc_password_required()
        if self is DocVersionsList404ResponseCode.DOC_PASSWORD_INCORRECT:
            return doc_password_incorrect()
        if self is DocVersionsList404ResponseCode.SHARE_PASSWORD_REQUIRED:
            return share_password_required()
        if self is DocVersionsList404ResponseCode.ABORTED:
            return aborted()
        if self is DocVersionsList404ResponseCode.NETWORK:
            return network()
        if self is DocVersionsList404ResponseCode.UNAUTHENTICATED:
            return unauthenticated()
        if self is DocVersionsList404ResponseCode.FORBIDDEN:
            return forbidden()
        if self is DocVersionsList404ResponseCode.NOT_FOUND:
            return not_found()
        if self is DocVersionsList404ResponseCode.WIRE_FORMAT:
            return wire_format()
        if self is DocVersionsList404ResponseCode.RUNTIME_UNAVAILABLE:
            return runtime_unavailable()
        if self is DocVersionsList404ResponseCode.INVALID_REFERENCE:
            return invalid_reference()
        if self is DocVersionsList404ResponseCode.WEAK_ANNOTATION_SESSION_CONFLICT:
            return weak_annotation_session_conflict()
        if self is DocVersionsList404ResponseCode.LAYER_VERSION_CONFLICT:
            return layer_version_conflict()
        if self is DocVersionsList404ResponseCode.NOT_IMPLEMENTED:
            return not_implemented()
        if self is DocVersionsList404ResponseCode.MALFORMED_PDF:
            return malformed_pdf()
        if self is DocVersionsList404ResponseCode.SIGNING_PENDING:
            return signing_pending()
        if self is DocVersionsList404ResponseCode.SIGNING_EXPIRED:
            return signing_expired()
        if self is DocVersionsList404ResponseCode.SIGNING_VERSION_MISMATCH:
            return signing_version_mismatch()
        if self is DocVersionsList404ResponseCode.SIGNATURE_REFUSED:
            return signature_refused()
        if self is DocVersionsList404ResponseCode.PROTECTED_DOCUMENT:
            return protected_document()
        if self is DocVersionsList404ResponseCode.STALE_BASE:
            return stale_base()
