from django.shortcuts import render
import random

# Create your views here.
lotto_ls = [34, 43, 18, 27, 40, 12, 17, 39, 1, 13, 14, 20, 33, 10, 45, 4, 19, 15, 31, 37, 11, 3, 5, 8, 24, 36, 38, 2, 21, 26, 44, 7, 42, 16, 25, 28, 6, 35, 41, 30, 29, 23, 32, 22, 9]

def index(request):
    return render(request, 'index.html')

def rec(request):
    if request.method == 'POST':
        nums_head = request.POST['nums_head']
        nums_tail = request.POST['nums_tail']
        # 빈 값 이거나 0일때, 45개 이상일 때 처리
        lotto_list = set()
        if nums_head != '' and nums_head != 0:
            nums_head = int(nums_head)
            if nums_head > 45:
                nums_head = 45
            for i in lotto_ls[:nums_head]:
                lotto_list.add(i)
        if nums_tail != '' and nums_tail != 0:
            nums_tail = int(nums_tail)
            if nums_tail > 45:
                nums_tail = 45
            for i in lotto_ls[-nums_tail:]:
                lotto_list.add(i)
        if len(lotto_list) < 6:
            message = {'message' : '최소 6개의 숫자가 되도록 올바른 숫자를 입력해주세요.'}
            return render(request, 'error.html', message)
        rec_ls = {
            'rec' : sorted(list(random.sample(lotto_list, 6))),
            'lotto_list' : list(lotto_list),
        }
        return render(request, 'recommend.html', rec_ls)
        
    return render(request, 'rec.html')