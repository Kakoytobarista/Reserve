menu = [
    {'title': 'Log out', 'url_name': 'logout'},
    {'title': 'Password change', 'url_name': 'password_change'},
    {'title': 'Weather', 'url_name': 'weather_page'},
    {'title': 'Workers', 'url_name': 'workers'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        context['menu'] = user_menu
        return context

