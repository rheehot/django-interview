"""
Django Middleware
"""

# ==============================================================================
# Django의 미들웨어 동작 원리
# ==============================================================================

## Q1. Django의 미들웨어 설정이 다음과 같습니다. Client에서 Request를 보낼 때
## 미들웨어 실행 순서를 나열해주세요.
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
