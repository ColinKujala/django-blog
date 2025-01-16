from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path("", PollListView().as_view(), name="poll_index"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll_detail"),
]

"""
Note to self:
    When you create the class-based view, you will need to instanciate the
    class and then do a call to as_view().
    BUT
    When you use the Django built-in class-based views, the as_view() call
    needs to be made on the class, not on an instance... that is why
    above you see my custom class based view instanciated and then as_view
    is called on it, whereas the Django built-in version doesn't instantiate
    first. PollDetailView.as_view()
"""
