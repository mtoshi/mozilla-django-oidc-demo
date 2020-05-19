# -*- coding: utf-8 -*-
"""api.views.rank."""

from django.conf import settings
from django.views.generic import View
from django.shortcuts import render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, View):

    """HomeView."""

    def get(self, request):
        """Get."""
        return render_to_response('home/index.html', {
            'request': request,
            'settings': settings,
        }, status=200)
