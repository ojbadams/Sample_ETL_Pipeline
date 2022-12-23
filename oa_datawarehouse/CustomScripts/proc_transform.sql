DELIMITER //
DROP PROCEDURE IF EXISTS Staging.proc_transform;
CREATE PROCEDURE Staging.proc_transform()
BEGIN

INSERT INTO Core.locations(commonName, lat, lon, id)
SELECT
    commonName,
    CAST(lat as FLOAT),
    CAST(lon as FLOAT),
    id
FROM Staging.locations
ON DUPLICATE KEY UPDATE
 commonName = VALUES(commonName),
 lat = VALUES(lat),
 lon = VALUES(lat),
 id = VALUES(id);

TRUNCATE Staging.locations;

END //