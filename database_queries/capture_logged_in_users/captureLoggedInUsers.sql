/*

This query compares the last login date of users with their last log out date, if the former is greater than the latter
then the user is currently logged in.

There is one caveat.  It will not capture first login of users because there is no log out date to compare against.

There is also an `in` exclusion list which contains a list of ids to ignore as they appear logged in but are not.
I just had the user to ignore and in the query below,

*/

select login.user_id, in_date, out_date from (select user_id, max(date_created) as in_date from audit_log
    where event_type = 'login#process' and user_id is not NULL group by user_id) as login, (select user_id, max(date_created) as out_date from audit_log
        where event_type = 'logout#index' and user_id is not NULL group by user_id) as logout where login.user_id = logout.user_id and in_date > out_date
            and login.user_id not in (3);