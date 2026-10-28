

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MimeTypes(enum.StrEnum):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/item-spec/item-spec.md#media-types
    """

    IMAGE_TIFF_APPLICATION_GEOTIFF = "image/tiff; application=geotiff"
    IMAGE_TIFF_APPLICATION_GEOTIFF_PROFILE_CLOUD_OPTIMIZED = "image/tiff; application=geotiff; profile=cloud-optimized"
    IMAGE_JP2 = "image/jp2"
    IMAGE_PNG = "image/png"
    IMAGE_JPEG = "image/jpeg"
    APPLICATION_GEO_JSON = "application/geo+json"
    APPLICATION_GEO_JSON_SEQ = "application/geo+json-seq"
    APPLICATION_GEOPACKAGE_SQLITE3 = "application/geopackage+sqlite3"
    APPLICATION_VND_GOOGLE_EARTH_KML_XML = "application/vnd.google-earth.kml+xml"
    APPLICATION_VND_GOOGLE_EARTH_KMZ = "application/vnd.google-earth.kmz"
    APPLICATION_X_PROTOBUF = "application/x-protobuf"
    APPLICATION_VND_MAPBOX_VECTOR_TILE = "application/vnd.mapbox-vector-tile"
    APPLICATION_X_HDF = "application/x-hdf"
    APPLICATION_X_HDF5 = "application/x-hdf5"
    APPLICATION_XML = "application/xml"
    APPLICATION_JSON = "application/json"
    APPLICATION_NDJSON = "application/ndjson"
    TEXT_HTML = "text/html"
    TEXT_PLAIN = "text/plain"
    APPLICATION_VND_OAI_OPENAPI_JSON_VERSION30 = "application/vnd.oai.openapi+json;version=3.0"
    APPLICATION_VND_OAI_OPENAPI_VERSION30 = "application/vnd.oai.openapi;version=3.0"
    APPLICATION_SCHEMA_JSON = "application/schema+json"
    APPLICATION_PDF = "application/pdf"
    TEXT_CSV = "text/csv"
    APPLICATION_VND_APACHE_PARQUET = "application/vnd.apache.parquet"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

    def visit(
        self,
        image_tiff_application_geotiff: typing.Callable[[], T_Result],
        image_tiff_application_geotiff_profile_cloud_optimized: typing.Callable[[], T_Result],
        image_jp2: typing.Callable[[], T_Result],
        image_png: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        application_geo_json: typing.Callable[[], T_Result],
        application_geo_json_seq: typing.Callable[[], T_Result],
        application_geopackage_sqlite3: typing.Callable[[], T_Result],
        application_vnd_google_earth_kml_xml: typing.Callable[[], T_Result],
        application_vnd_google_earth_kmz: typing.Callable[[], T_Result],
        application_x_protobuf: typing.Callable[[], T_Result],
        application_vnd_mapbox_vector_tile: typing.Callable[[], T_Result],
        application_x_hdf: typing.Callable[[], T_Result],
        application_x_hdf5: typing.Callable[[], T_Result],
        application_xml: typing.Callable[[], T_Result],
        application_json: typing.Callable[[], T_Result],
        application_ndjson: typing.Callable[[], T_Result],
        text_html: typing.Callable[[], T_Result],
        text_plain: typing.Callable[[], T_Result],
        application_vnd_oai_openapi_json_version30: typing.Callable[[], T_Result],
        application_vnd_oai_openapi_version30: typing.Callable[[], T_Result],
        application_schema_json: typing.Callable[[], T_Result],
        application_pdf: typing.Callable[[], T_Result],
        text_csv: typing.Callable[[], T_Result],
        application_vnd_apache_parquet: typing.Callable[[], T_Result],
        application_octet_stream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MimeTypes.IMAGE_TIFF_APPLICATION_GEOTIFF:
            return image_tiff_application_geotiff()
        if self is MimeTypes.IMAGE_TIFF_APPLICATION_GEOTIFF_PROFILE_CLOUD_OPTIMIZED:
            return image_tiff_application_geotiff_profile_cloud_optimized()
        if self is MimeTypes.IMAGE_JP2:
            return image_jp2()
        if self is MimeTypes.IMAGE_PNG:
            return image_png()
        if self is MimeTypes.IMAGE_JPEG:
            return image_jpeg()
        if self is MimeTypes.APPLICATION_GEO_JSON:
            return application_geo_json()
        if self is MimeTypes.APPLICATION_GEO_JSON_SEQ:
            return application_geo_json_seq()
        if self is MimeTypes.APPLICATION_GEOPACKAGE_SQLITE3:
            return application_geopackage_sqlite3()
        if self is MimeTypes.APPLICATION_VND_GOOGLE_EARTH_KML_XML:
            return application_vnd_google_earth_kml_xml()
        if self is MimeTypes.APPLICATION_VND_GOOGLE_EARTH_KMZ:
            return application_vnd_google_earth_kmz()
        if self is MimeTypes.APPLICATION_X_PROTOBUF:
            return application_x_protobuf()
        if self is MimeTypes.APPLICATION_VND_MAPBOX_VECTOR_TILE:
            return application_vnd_mapbox_vector_tile()
        if self is MimeTypes.APPLICATION_X_HDF:
            return application_x_hdf()
        if self is MimeTypes.APPLICATION_X_HDF5:
            return application_x_hdf5()
        if self is MimeTypes.APPLICATION_XML:
            return application_xml()
        if self is MimeTypes.APPLICATION_JSON:
            return application_json()
        if self is MimeTypes.APPLICATION_NDJSON:
            return application_ndjson()
        if self is MimeTypes.TEXT_HTML:
            return text_html()
        if self is MimeTypes.TEXT_PLAIN:
            return text_plain()
        if self is MimeTypes.APPLICATION_VND_OAI_OPENAPI_JSON_VERSION30:
            return application_vnd_oai_openapi_json_version30()
        if self is MimeTypes.APPLICATION_VND_OAI_OPENAPI_VERSION30:
            return application_vnd_oai_openapi_version30()
        if self is MimeTypes.APPLICATION_SCHEMA_JSON:
            return application_schema_json()
        if self is MimeTypes.APPLICATION_PDF:
            return application_pdf()
        if self is MimeTypes.TEXT_CSV:
            return text_csv()
        if self is MimeTypes.APPLICATION_VND_APACHE_PARQUET:
            return application_vnd_apache_parquet()
        if self is MimeTypes.APPLICATION_OCTET_STREAM:
            return application_octet_stream()
