# -*- coding: utf-8 -*-
"""api.views.rank."""

from django.conf import settings
from django.views.generic import View
from django.shortcuts import render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.models import Session


class HomeView(LoginRequiredMixin, View):

    """HomeView."""

    def get(self, request):
        """Get."""
        sessionid = request.COOKIES['sessionid']
        session = Session.objects.get(pk=sessionid)
        session_data = session.get_decoded()
        return render_to_response('home/index.html', {
            'request': request,
            'settings': settings,
            'session_data': session_data,
        }, status=200)
