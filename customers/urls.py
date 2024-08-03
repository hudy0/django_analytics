from customers import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"customers", views.CustomerViewSet)
