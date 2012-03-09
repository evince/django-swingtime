from django.conf.urls.defaults import *

from swingtime import views


urlpatterns = patterns('',
    url(r'^(?:calendar/)?$',
        view=views.today_view,
        name='swingtime-today'),

    url(r'^calendar/(?P<year>\d{4})/$',
        view=views.year_view,
        name='swingtime-yearly-view'),

    url(r'^calendar/(\d{4})/(0?[1-9]|1[012])/$',
        view=views.month_view,
        name='swingtime-monthly-view'),

    url(r'^calendar/(\d{4})/(0?[1-9]|1[012])/([0-3]?\d)/$',
        view=views.day_view,
        name='swingtime-daily-view'),

    url(r'^events/$',
        view=views.event_listing,
        name='swingtime-events'),

    url(r'^events/add/$',
        view=views.add_event,
        name='swingtime-add-event'),

    url(r'^events/(\d+)/$',
        view=views.event_view,
        name='swingtime-event'),

    url(r'^events/(\d+)/(\d+)/$',
        view=views.occurrence_view,
        name='swingtime-occurrence'),
)
