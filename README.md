## Flask + MongoDB Basic User Authentication Tutorial

Accompanying video: https://youtu.be/evarMujBC88

This is a basic Flask + MongoDB project that implements user authentication. 
It's intended for learning, or to use as a starting point. It is not intended
to be feature complete or pretty. It is intended to follow best practices for
password storage and checking.

A User model is defined for convenient integration into other parts of the code.

A CLI script `register.py` is provided for creating users and updating passwords.

To use it:
```
python register.py --username your_username_here
```
It will prompt for your password, type it and then press enter, it won't show the password as you type.


### Going Further? 

Here are some ideas for ways to enhance or expand upon the system. If you'd like to see videos
covering any of these topics please leave a comment on YT video or create an issue on GitHub.

- Frontend Registration Form and Flask Route Function
- Logout Functionality
- User Activation Mechanism w/ emailed activation link
- Forgot password functionality

### Found a Bug or Have an Improvement Idea?
Please open an issue on github describing the bug or idea that you have.