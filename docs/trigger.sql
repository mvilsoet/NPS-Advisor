insert into Events(datestart, dateend, eventid)
values (NULL, '2022-11-11', 'abbafoogi');
select * from Events where eventid = 'abbafoogi';

delete from Events where eventid = 'abbafoogi'

drop trigger if exists cleanUpAddEvent;
DELIMITER $$
create trigger cleanUpAddEvent before insert on Events
for each row
begin
    if new.description is null or new.description = ''
    then set new.description = 'Add a description here!';
    end if;
    if new.datestart is null
    then set new.datestart = CAST(NOW() As Date);
    end if;
    if new.dateend is null
    then set new.dateend = CAST(NOW() As Date);
    end if;
    if new.datestart > new.dateend
    then set new.dateend = new.datestart;
    end if;
    if new.title is null or new.title = ''
    then set new.title = 'Untitled event; add a bloody title m8!';
    end if;
end;
$$
DELIMITER ;