
""""Code Review:
    1- instead of If-statement would be better to query the model with filter.
    2- changing logger level to DEBUG and using info instead of warning.
    3- typo in Info : doen't -> doesn't
    4- there is no error handling in this function
    5- there is no return.
    6- naming function can be better.
    7- Use Docstring for more information about the function.
"""



def get_admin_prefs():
   admin_users = User.objects.filter(is_staff=True)
   admins_with_preferences = []
   if admin_users:
       for user in admin_users:
           if user.preference.id:
               admins_with_preferences.append(user)
               logger.info(f"{user}  has preferences")
           else:
               logger.info(f"{user} doesn't has any preferences")
    else:
        logger.info("No user")





""" Alternative of this function """
def get_admin_with_prefs():
    """This function will return list of all admin users that have preference id"""
    try:
        admin_users = User.objects.filter(is_staff=True)
        admins_with_preferences = [ admin for admin in admin_users if admin.preference.id]
        return admins_with_preferences
    except Exception as err:
        logging.error(err)