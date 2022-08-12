###### 오늘 수업 끝에 와서 고칠거에요. 되게! ######
print("비가 오나요? 오면 1, 안 오면 0을 입력하세요.")
rain = input()  # 비가 온다 1, 비가 안 온다 0
print(type(rain))

print("눈은 오나요? 오면 1, 안 오면 0을 입력하세요.")
snow = input()  # 눈이 온다 1, 눈이 안 온다 0
print(snow)

if rain == 1:
    print("비가 옵니다.")


if rain == 1 or snow == 1:
    print("약속을 취소하고 집에서 디즈니 플러스 볼게요.")