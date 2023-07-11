/*
This query compares the last login date of users with their last log out date, if the former is greater than the latter
then the user is currently logged in.

The union query also allows it to capture new users who have logged in, but not yet logged out.

Computes session_mins
*/

select login.user_id, in_date, TIMESTAMPDIFF(MINUTE, in_date, now()) as session_mins from (select user_id, max(date_created) as in_date from audit_log where event_type = 'login#process'
    and user_id is not NULL group by user_id) as login inner join (select user_id, max(date_created) as out_date from audit_log where event_type = 'logout#index' and user_id is not NULL group by user_id) as logout
        on login.user_id = logout.user_id where in_date > out_date
union(
    select login.user_id, in_date, TIMESTAMPDIFF(MINUTE, in_date, now()) as session_mins from (select user_id, max(date_created) as in_date from audit_log where event_type = 'login#process'
        and user_id is not NULL group by user_id) as login where  login.user_id not in (select user_id from audit_log where event_type = 'logout#index' and user_id is not NULL group by user_id)
);