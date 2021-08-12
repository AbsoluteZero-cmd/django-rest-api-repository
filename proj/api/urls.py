from rest_framework.routers import SimpleRouter

from api.views import QuestionViewSet

router = SimpleRouter()
router.register(r'questions', viewset=QuestionViewSet)

app_name = 'api'
urlpatterns = [
]

urlpatterns += router.urls