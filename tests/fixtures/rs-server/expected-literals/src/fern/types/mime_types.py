

import typing

MimeTypes = typing.Union[
    typing.Literal[
        "image/tiff; application=geotiff",
        "image/tiff; application=geotiff; profile=cloud-optimized",
        "image/jp2",
        "image/png",
        "image/jpeg",
        "application/geo+json",
        "application/geo+json-seq",
        "application/geopackage+sqlite3",
        "application/vnd.google-earth.kml+xml",
        "application/vnd.google-earth.kmz",
        "application/x-protobuf",
        "application/vnd.mapbox-vector-tile",
        "application/x-hdf",
        "application/x-hdf5",
        "application/xml",
        "application/json",
        "application/ndjson",
        "text/html",
        "text/plain",
        "application/vnd.oai.openapi+json;version=3.0",
        "application/vnd.oai.openapi;version=3.0",
        "application/schema+json",
        "application/pdf",
        "text/csv",
        "application/vnd.apache.parquet",
        "application/octet-stream",
    ],
    typing.Any,
]
