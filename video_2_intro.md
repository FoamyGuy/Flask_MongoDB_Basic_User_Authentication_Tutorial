
## Great Talk Explaining The Concepts 
You should watch Philippe De Ryck Talk From NDC Oslo 2024 "SEVEN things about API security"
https://www.youtube.com/watch?v=QBMgAOKrdes

## Lowest Hanging Fruit
Observable inconsistent return values or status codes that are correlated to different
possible outcomes of the login attempt. i.e. If the user attempts to login with a 
non-existent username and the server returns an error stating "User doesn't exist". But
on the same system if the user attempts to login with a valid existing username but the
incorrect password the system responds with an error stating "Password was invalid". 

These observable differences can allow an attacker to guess usernames at random or using
databases stolen from other companies and services and discern which if any are valid 
users within your system.

The best practice is to return a consistent and generic error message with no observable
differences i.e. always return "Username or password is invalid" no matter what the true
reason for failed login was.

## Slightly Higher Fruit: Timing Attacks
Discussed in the video starting around:
20:40 https://youtu.be/QBMgAOKrdes?si=p2EBRqd0IaERJCN4&t=1240

A timing attack exploits login view logic that is written to "return early" if 
the username given for a login attempt does not exist in the database. Often 
this is caused by the view checking first if the username exists, returning an 
error immediately if it does not. Then only after ensuring it exists the view 
computes the hash of the incoming password and validates it against the hash
stored in the database. Hashing is a relatively time-consuming process compared
to many other tasks that modern computers carry out. 

If the view logic computes a hash only when it finds a valid username and not
when it doesn't then it's likely that an attacker can notice the inconsistent 
response timings and thus glean information about whether the guessed user account
exists or not. 

One simple solution is to always compute a hash inside the login view, even when
the provided username is invalid. 
