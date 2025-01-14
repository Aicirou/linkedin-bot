from linkedin_bot import LinkedInBot

if __name__ == "__main__":
    bot = LinkedInBot()
    if bot.login():
        print("Successfully logged in")
        bot.search_jobs("Data Engineer", "Noida, Uttar Pradesh, India")
        bot.filter_jobs()
        bot.apply_to_jobs()
    else:
        print("Login failed")
    bot.close()
