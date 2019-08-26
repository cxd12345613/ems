from django.shortcuts import render,HttpResponse
import  random,string
##从image.py中导入导入ImageCaptcha类
from security_app.captcha.image import ImageCaptcha

##获取验证码
def getcaptcha(request):

    #声明一个图片验证码对象
    image=ImageCaptcha()
    #随机码：大小写英文字母+数字，随机抽取5位作为验证码
    code=random.sample(string.ascii_letters+string.digits,5)
    #将生成的随机字符拼接成字符串
    random_code="".join(code)
    print(random_code)
    # 将验证码生存如session，以备后续验证
    request.session['code']=random_code
    #将字符串作为验证码图片中的文本
    date=image.generate(random_code)
    #写出验证码给客户端
    return HttpResponse(date,'image/png')



