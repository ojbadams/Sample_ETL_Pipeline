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
FROM Staging.locations;

TRUNCATE Staging.locations;

END //