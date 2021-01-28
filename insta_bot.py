from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("image.jpg", caption="caption")

######  follow someone #######
bot.follow("username")

######  send a message #######
bot.send_message("Hello from me", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("username")
for follower in my_followers:
    print(follower)

######  unfollow all #######
bot.unfollow_everyone()