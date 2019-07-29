"""
Django ORM Optimization.
"""

# ==============================================================================
# Querysets의 Lazy evaluation
# ==============================================================================

## Q1. 각각의 케이스에서 몇 번의 SQL이 실행되는지 말해주세요.

### CASE1
for user in User.objects.all():
    # 로직...

### CASE2
users = User.objects.all()

### CASE3
user = User.objects.all()[1]

### CASE4
[user for user in User.objects.all()]

### CASE5
print([user for user in User.objects.all()])
print([user for user in User.objects.all()])

### CASE6
queryset = User.objects.all()
print(queryset[1])
print(queryset[1])

### CASE7
queryset = User.objects.all()
print([user.name for user in queryset])
print([user.name for user in queryset])

### CASE8
queryset = User.objects.all()
list(queryset)
print(queryset[1])
print(queryset[1])

### CASE9
user = User.objecst.get(id=10)
user.social
user.social

### CASE10
user = User.objects.get(id=10)
user.social.all()
user.social.all()

# ==============================================================================
# Queryset 최적화
# ==============================================================================
## Q2. count1과 count2의 차이점에 대해 말해주세요.
count1 = len(User.objects.all())
count2 = User.objects.count()

## Q3. exists1과 exists2의 차이점에 대해 말해주세요.
exists1 = len(User.objects.all()) > 0
exists2 = User.objects.exists()

## Q4. 다음 실행문의 문제점은 무엇인가요? 그리고 개선된 실행문을 알려주세요.
for user in User.objects.all():
    user.is_active = True
    user.save()

## Q5. 아래 두 문장의 차이점에 대해 설명해주세요.
social_id = User.objects.get(id=1).social.id
social_id = User.objects.get(id=1).social_id

## Q6. 다음 실행문의 문제점에 대해 말해주세요. 그리고 개선된 실행문을 알려주세요.
active = {
    user.name: user.is_active
    for user in User.objects.all()
}

## Q7. 다음 실행문의 문제점에 대해 말해주세요. 그리고 개선된 실행문을 알려주세요.
for user in User.objects.all():
    if user.is_active:
        # Do something

## Q8. 다음 실행문의 문제점에 대해 말해주세요. 그리고 개선된 실행문을 알려주세요.
for user in User.objects.all():
    user.logged_count += 1
    user.save()

## Q9. 다음 실행문의 문제점에 대해 말해주세요. 그리고 개선된 실행문을 알려주세요.
min_count = 0
for user in User.objects.all():
    if user.count < min_count:
        min_count = user.count

## Q10. 다음 실행문의 문제점에 대해 말해주세요. 그리고 개선된 실행문을 알려주세요.
nice_users = User.objects.filter(
    is_active=True
)
for count in range(18):
    user = nice_users.get(logged_count=count)
