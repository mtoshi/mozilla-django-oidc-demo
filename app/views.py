# -*- coding: utf-8 -*-
"""app.viewes"""

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):

    """HomeView."""

    template_name = "home/index.html"
