#encoding:utf-8

subreddit = 'football+liverpoolfc+coys+soccernerd+footballhighlights+chelseafc+atletico+realmadrid'
t_channel = '@soccerx'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
