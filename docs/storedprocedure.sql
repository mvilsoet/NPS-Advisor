drop procedure if exists bingChillingBepis;

DELIMITER $$
create procedure bingChillingBepis()
BEGIN
    DECLARE parkName varchar(1024);
    DECLARE numEvents int;
    DECLARE pDescript VARCHAR(1024);
    DECLARE pState VARCHAR(1024);
    DECLARE pDirs VARCHAR(1024);
    
    DECLARE condA bool;
    DECLARE condB bool;
    
    DECLARE finished int default 0;
    
    DECLARE cur CURSOR FOR
        SELECT Events.parkfullname, Parks.stateAbbr, Parks.description, Parks.directionsUrl, COUNT(eventid)
        FROM Events join Parks on (Events.parkfullname = Parks.name)
        WHERE datestart <= CAST(DATE_ADD(NOW(), INTERVAL 7 DAY) As Date)
        and dateend >= CAST(NOW() as Date)
        GROUP BY Parks.parkCode;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
    
    drop table if exists TEMP_PROC;
    create table TEMP_PROC(name VARCHAR(1024) PRIMARY KEY, description VARCHAR(1024), stateAbbr VARCHAR(1024), directionsUrl VARCHAR(1024));
    OPEN cur;

    l: loop
        if finished then leave l;
        end if;
        fetch cur into parkName, pState, pDescript, pDirs, numEvents;
        set condA = numEvents > 3;
        set condB = parkName in (select Parks.name from (SELECT DISTINCT s.parkCode FROM ParkingLots s WHERE s.hasFee = 0) as freeParking join Parks on (freeParking.parkCode = Parks.parkCode));
        if condA or condB
        then insert ignore into TEMP_PROC values (parkName, pDescript, pState, pDirs);
        end if;
    end loop l;
    CLOSE cur;

    SELECT * from TEMP_PROC;
END
$$
Delimiter ;