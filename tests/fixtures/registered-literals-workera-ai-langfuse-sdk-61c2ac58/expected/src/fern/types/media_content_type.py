

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MediaContentType(enum.StrEnum):
    """
    The MIME type of the media record
    """

    IMAGE_PNG = "image/png"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_JPG = "image/jpg"
    IMAGE_WEBP = "image/webp"
    IMAGE_GIF = "image/gif"
    IMAGE_SVG_XML = "image/svg+xml"
    IMAGE_TIFF = "image/tiff"
    IMAGE_BMP = "image/bmp"
    AUDIO_MPEG = "audio/mpeg"
    AUDIO_MP3 = "audio/mp3"
    AUDIO_WAV = "audio/wav"
    AUDIO_OGG = "audio/ogg"
    AUDIO_OGA = "audio/oga"
    AUDIO_AAC = "audio/aac"
    AUDIO_MP4 = "audio/mp4"
    AUDIO_FLAC = "audio/flac"
    VIDEO_MP4 = "video/mp4"
    VIDEO_WEBM = "video/webm"
    TEXT_PLAIN = "text/plain"
    TEXT_HTML = "text/html"
    TEXT_CSS = "text/css"
    TEXT_CSV = "text/csv"
    APPLICATION_PDF = "application/pdf"
    APPLICATION_MSWORD = "application/msword"
    APPLICATION_VND_MS_EXCEL = "application/vnd.ms-excel"
    APPLICATION_ZIP = "application/zip"
    APPLICATION_JSON = "application/json"
    APPLICATION_XML = "application/xml"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

    def visit(
        self,
        image_png: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        image_jpg: typing.Callable[[], T_Result],
        image_webp: typing.Callable[[], T_Result],
        image_gif: typing.Callable[[], T_Result],
        image_svg_xml: typing.Callable[[], T_Result],
        image_tiff: typing.Callable[[], T_Result],
        image_bmp: typing.Callable[[], T_Result],
        audio_mpeg: typing.Callable[[], T_Result],
        audio_mp3: typing.Callable[[], T_Result],
        audio_wav: typing.Callable[[], T_Result],
        audio_ogg: typing.Callable[[], T_Result],
        audio_oga: typing.Callable[[], T_Result],
        audio_aac: typing.Callable[[], T_Result],
        audio_mp4: typing.Callable[[], T_Result],
        audio_flac: typing.Callable[[], T_Result],
        video_mp4: typing.Callable[[], T_Result],
        video_webm: typing.Callable[[], T_Result],
        text_plain: typing.Callable[[], T_Result],
        text_html: typing.Callable[[], T_Result],
        text_css: typing.Callable[[], T_Result],
        text_csv: typing.Callable[[], T_Result],
        application_pdf: typing.Callable[[], T_Result],
        application_msword: typing.Callable[[], T_Result],
        application_vnd_ms_excel: typing.Callable[[], T_Result],
        application_zip: typing.Callable[[], T_Result],
        application_json: typing.Callable[[], T_Result],
        application_xml: typing.Callable[[], T_Result],
        application_octet_stream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MediaContentType.IMAGE_PNG:
            return image_png()
        if self is MediaContentType.IMAGE_JPEG:
            return image_jpeg()
        if self is MediaContentType.IMAGE_JPG:
            return image_jpg()
        if self is MediaContentType.IMAGE_WEBP:
            return image_webp()
        if self is MediaContentType.IMAGE_GIF:
            return image_gif()
        if self is MediaContentType.IMAGE_SVG_XML:
            return image_svg_xml()
        if self is MediaContentType.IMAGE_TIFF:
            return image_tiff()
        if self is MediaContentType.IMAGE_BMP:
            return image_bmp()
        if self is MediaContentType.AUDIO_MPEG:
            return audio_mpeg()
        if self is MediaContentType.AUDIO_MP3:
            return audio_mp3()
        if self is MediaContentType.AUDIO_WAV:
            return audio_wav()
        if self is MediaContentType.AUDIO_OGG:
            return audio_ogg()
        if self is MediaContentType.AUDIO_OGA:
            return audio_oga()
        if self is MediaContentType.AUDIO_AAC:
            return audio_aac()
        if self is MediaContentType.AUDIO_MP4:
            return audio_mp4()
        if self is MediaContentType.AUDIO_FLAC:
            return audio_flac()
        if self is MediaContentType.VIDEO_MP4:
            return video_mp4()
        if self is MediaContentType.VIDEO_WEBM:
            return video_webm()
        if self is MediaContentType.TEXT_PLAIN:
            return text_plain()
        if self is MediaContentType.TEXT_HTML:
            return text_html()
        if self is MediaContentType.TEXT_CSS:
            return text_css()
        if self is MediaContentType.TEXT_CSV:
            return text_csv()
        if self is MediaContentType.APPLICATION_PDF:
            return application_pdf()
        if self is MediaContentType.APPLICATION_MSWORD:
            return application_msword()
        if self is MediaContentType.APPLICATION_VND_MS_EXCEL:
            return application_vnd_ms_excel()
        if self is MediaContentType.APPLICATION_ZIP:
            return application_zip()
        if self is MediaContentType.APPLICATION_JSON:
            return application_json()
        if self is MediaContentType.APPLICATION_XML:
            return application_xml()
        if self is MediaContentType.APPLICATION_OCTET_STREAM:
            return application_octet_stream()
