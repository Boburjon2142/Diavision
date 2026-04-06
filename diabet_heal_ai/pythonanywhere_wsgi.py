"""
PythonAnywhere uchun namunaviy WSGI konfiguratsiya.
Bu fayldagi yo‘llarni o‘z akkauntingizga moslab yangilang.
"""
import os
import sys
from pathlib import Path

project_home = Path("/home/yourusername/diabet-AI")
if project_home.exists():
    sys.path.insert(0, str(project_home))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "diabet_heal_ai.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

application = get_wsgi_application()
