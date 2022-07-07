from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class RiderRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.user_rider
