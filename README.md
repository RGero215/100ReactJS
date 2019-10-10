# 100ReactJS

# API End Points 

## Blog
/blog/api/
/blog/api/postAPI/

## Marketing Tournament Group Tournament
/marketing/api/
/marketing/api/groupsAPI/

## Pomodoro
/pomodoro/api/
/pomodoro/api/pomodoroAPI/

## Stats
/stats/api/
/stats/api/statisticsAPI/
/stats/api/onePlayerAPI/
/stats/api/twoGamesAPI/

## Test
/api/
/api/testAPI/

## Tournament of Four and Group Pomodoro of Four
/tournament/api/
/tournament/api/fourPlayersAPI/
GET /tournament/api/fourPomodoroAPI/

## User and Profile
/profile/api/
/profile/api/profileAPI/
/profile/api/userAPI/
/profile/api/loginAPI/
/profile/api/userRegisterAPI/

## User Pomodoros
/pomodoro/api/user/ID/
example: /pomodoro/api/user/1/

## All routes require token except /loginAPI/ and /userRegisterAPI/ 
### Include token in the heather as key value pair. Ex:
{
    "Authorization": "Token b39caa41531228e02714c075fef300bd5419370f"
}
### Token are created when user register and also in the login form for existing user in production without token the first time they login. After that login will filter token by user id.

