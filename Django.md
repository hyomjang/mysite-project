## Django Day 1

* mv 폴더명 바꾸기
	* mv 예전폴더명 바꿀폴더명
	* mv blog project-blog
	* 
* pwd
* rm -rf .
* ls -al --> 안보이는 파일도 보여짐

* django-admin startproject blog

* python manage.py startapp post
* python manage.py makemigrations
  * 하면 no change detected 라고 나옴
  * settings.py에서 installed_apps에 'post'설정을 줘야된다

* python manage.py runserver

* models.py에서 변경되었을때 manage.py migrate한다
*  db로 보내는 게 migrate
*  쌓인 데이타를 다루는게 orm
* 	* Post.objects.all()
*  	- 여기 모델에 있는 모든 데이터를 불러온다
*   djanggo template 에는 {}안에 for문을 
brew install pyenv
pyenv install 3.4.3
pyenv virtualenv 3.4.3 fc-blog

10/5

**html 파일에서 {{ post.description }}**

* 여기서 dot . aren't used only for attribute lookup
* They also can do dictionary-key lookup, index lookup, function calls

**Staticfiles**

* settings.py
	* STATICFILES_DIRS-  static file 위치한 경로 directory 설정
	* STATIC_URL 
		* 웹 페이지에서 사용할 정적 파일의 최상위 URL 경로
		* 실제 파일이나 디렉터리가 아니며 이용자 마음대로 정해도 무방
	* STATIC_ROOT 
		* Django project에서 사용하는 모든 정적파일을 모아넣는 경로 

> manage.py findstatic -> STATICFILES_DIRS에 설정한 경로에서 지정한 정적 파일을 찾는다.

* findstatic 명령어로 탐색되는 정적 파일 경로에 static_URL 경로를 합치면 실제 웹에서 접근 가능한 URL
	*	ex) http://127.0.0.1:8000/static/css/post_list.css

### Django Project  

* **include()** chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing
* **Foreignkey** each Choice is related to a single Questions
	* ex) models.ForeignKey(Question) 

```sh
$ python manage.py sqlmigrate polls 0001
$ python manage.py check
```
The **sqlmigrate command** doesn’t actually run the migration on your database - it just prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

* Run python manage.py makemigrations to create migrations for those changes
* Run python manage.py migrate to apply those changes to the database.
* get_object_or_404()



**Difference between render, render_to_response, direct_to_template**

	
	
##DAY2

* include를 사용하는 url에는 맨뒤에 $를 사용하지않는다
* mysite urls.py 에서 polls 를 지정했기때문에 polls.urls.py url이 ^$이여도 polls로 지정이된다
* Question.objects.order_by('-pub_date') ---내림차순
* pub_date' ---오름차순
* **/**polls/ ----> '/' 는 루트부터 시작한다라는뜻
	* http://127.0.0.1:8000/polls/ 	
* loader.get_template (index.html)
	*  loader가 app내에있는 template 을 찾아서 (index.html)를 불러준다
*  primary key == 똑같은 name을 가지지만 id는 각 data당 하나의 고유의 number를 받기때문에 ,, 지정하기 위해 primary key 를지정
*  template 에서는 question.choice_set.all() 을 사용할때 ()를**안한다**
*  template에는 question_id 가 아닌 question.id 를사용한다
	* template 에는 (.) 형식만 사용 가능하다 
*  reverse : template --? **{ %url %} tag를 사용**
			* views.py 에는 **reverse('polls:result')  **
			* 	
* django forloop counter - {%for in  %} {%end in %} 안에 사용 
	* for 문도는 횟수에 따라 숫자를 count (기본적으로 1부터시작
	* 0부터 시작하려면 forloop 0	 	


## Day 3
###Models

primary key 지정

* num = models.**AutoField(primary_key = True)**
* blank - 장고에서 다룸   null- db에서 처리
	* 둘다 default= false -->blank나  null을하면 error를 띄운다.
*  p = Person(name="Fred Flintstone", shirt_size="L")
	* p.save()
	* p.shirt_size
		'L'
	* p.get_shirt_size_display()
'Large'
* objects.create() 하면 save()안해도 저장됨
* primary key를 지정하면 원래 값을 바꿔도 pk지정한 값은 변경되지않음
	* 다른  id에 생성 



## Day 4

추상 클래스 (Abstract Class)

(Query)
**get**

- 1개만 가지고온다
- data가 두개이상이면 error

**filter**

- 2개이상의 data를 가지고온다

**__ <-는 filter instance 뒤에 붙여서 꾸며준다**

**__exact**

> Entry.objects.get(headline__exact = 'Cat bites dog')


**__iexact**

* case- insensitive match
> Blog.objects.get(name__iexact = 'beatles blog')
>

**__contains**

**__gt**

* greater than
> Entry.objects.filter(id__gt = 4)

__startswith = '', __endswith = '', __lt = , __lte = 


**F expressions**

from django.db.models import F
> Entry.objects.filter(n_comments__gt = F('n_pingbacks')*2)
* 특정 모델 필드랑 다른 필드 값 비교할때 쓴다
* 필드를 비교

Q objects

from django.db.models import Q
> and 나 or 를 사용할때 양쪽 비교값을 비교할때 Q로 묶는다


```sh
Blog.objects.filter(entry__headline__contains='', entry__pub_date__year=2008)
```
* 

```sh
Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
```
* 두개의 차이점은 -> 첫번째는 lennon과 2008을 동시에 filter하고 두번째는 lennon을 filter 하고 나중에 2008 을 filter 한다
* 만약 lennon filter를 해서 100개중 20개가 남으면나중에 20개중에 2008 을 filter 한다

* block / extends 

 base.html 을 따로 베이스로 만들고 안에 컨텐츠들만 바뀐다했을때 다른 html 파일을 만들어서 컨텐츠만 따로 관리( extends base.html )



* {{post.text|linebreaksbr}}	
	* 줄바꿈을

	
	
	 
```sh
HttpResponseRedirect(reverse('polls:results', args=(question.id,)))	
```
====
```sh
return redirect('view이름' = URL pattern namespace + name or the callable view object, question_id = question.id)	 
```

* ModelForm
	*	모델에 정의한 field들을 참조하여 모델 폼을을 만들어주는 역할을한다.
```sh
class PhotoForm(forms.ModelForm): 	
	class Meta:
		model = Photo
		fields = ['title','image','description']


* LogIN
	* 내가 네이버로그인을하고 네이버는 다른사이트를 불러올때 계속 로그인인 상태를 보여준다. 이 각각은 연결 되어있지않다. 제가 요청을 한번보내면 받은사람은 다시보내고 그리고 다시한번 요청을 보낼때 서버는 내가 로그인이 되어있다는 사실을 알아야한다.
		* session 이란 서버가 해단 서버로 request(접근한) 클라이언트를 식별하는 방법	
		* 이것을 session으로 처리를한다. 특정한 key 값을 서버와 클라이언트 쪽에서 동시에 받는다. USER가 로그인을 할때 서버쪽에서  어떤 특정한 key값을 준다. 이 유저는 이key값과 mapping된다라고 서버는 처리를한다. 그리고 이 key값을 던져주면 클라이언트는 이key값을 가지고있는다. (브라우저에는 쿠키쪽에 넣어서 그 특정한 문자를 가지고있는다) 해당사이트를 활동할때 그 쿠키값을 계속 전달을해준다 서버는 그 문자를 받으면 '아 너가 걔야' 하면서 요청을 처리해준다.
		* auth_login에서 session id를 만들어주고 middleware에서 session id 를 처리를해주는역할을하게한다

		
* command+shift+F
	* find and replace all


* Messages framework
	* 글삭제했을때, 로그인 성공할때 잠깐 팝업뜨고 사라지는것을 사용할때 
	*  

* Unique
	* 한번field에 들어가면 중복 입력 불가능	


* AUTH_USER_MODEL = 'member.MyUser'
* BaseUserManager
	* create_user& create_superuser 를 가지고있고
	* create_user 와다르게 superuser로 생성할때는 무조건 password를 provide 해야한다 

* HASH
	* 비밀번호는 암호화를 통해 (특정화 함수를 통해 고정적인 

Client	------------------- Server

signup (string)----Hash---> password encrypted




**Session과 Cookie**

기본적으로 HTTP는 Stateless(페이지를 이동할 때마다 새로운 연결로 인식합니다.)합니다. 사용자의 요청에 대한 응답을 한 후 페이지 간의 연결을 해제하게 되는 것입니다. 이러할 경우, 로그인 정보가 기억되지 못하고 바로 소멸되기 때문에 이러한 클라이언트의 정보 유지를 위해 사용되는 것이 바로 세션과 쿠키입니다.

Session

SID를 식별자로 서버에 데이터를 저장하며, SID로는 쿠키나 도메인 파라미터를 이용하게 됩니다. 데이터는 서버 내의 파일이나 DB에 저장됩니다. (바로 이 저장 위치가 쿠키와 세션을 구분하는 가장 큰 차이점입니다.)

Cookie

쿠키는 클라이언트(웹브라우저)에 데이터를 저장합니다. 클라이언트 측에 저장을 하기 때문에 이를 해결하기 위해 제안된 것이 Session입니다. 현재는 Session이 더 많이 사용되고 있다고 합니다.


## LogIn / SignUP 

#### NoForm /Form/ ModelForm 

* NoForm
	* views 와 templates 에서만 작업
	* templates에 화면에 보여줄 form 형식을일일이 작성
	* views에 내가 따로 customizing 한 user model에 받은 data를 넣는 코드 작성

* Form
	* forms.py에 따로 forms.Form으로부터 상속받은 form class를 생성
	* views.py에서는 form= signupForm(request.POST) --> forms.is_valid()
	* NoForm과 똑같이 받은data를 user model에 넣는다.

* ModelForm
	* user model로 부터 상속 받은


#### Customizing User Model



## Day 12

# Email

[Django Email](https://docs.djangoproject.com/en/1.10/topics/email/)

-

# SMS API

[coolsms](http://www.coolsms.co.kr/)  
[Python SDK사용법](http://www.coolsms.co.kr/Python_SDK_Start_here)  


-

# 서버 세팅

### 연결 구조

- 도메인에 Cloudflare의 네임서버 사용
- Cloudflare의 DNS세팅에 접속할 IP세팅

-


#### 네임서버  

http://lhy.kr과 같은 도메인을 238.128.013.223과 같은 IP주소로 매핑시켜주는 서버  
네임서버를 관리하는 서버가 최상위 레벨이어야 변경시 적용이 빠름

#### A레코드와 CNAME의 차이

- A레코드
	- IP주소를 통해 직접 연결
- C레코드
	- 도메인으로 연결 후 해당 도메인의 IP주소를 다시 찾음

-

#### CDN

**Content Distribution Network**  
대용량 파일들을 분산된 서버로 운영하여, 요청에서 가까운 지역의 서버에서 전송해주는 서비스

-




### sending Email

* smtp server
	* SMTP프로토콜이란?
컴퓨터로 E-Mail을 보낼때, sendmail이나 qmail 등의 메일서버프로그램들이 사용된다. 이 프로그램은 사용자 또는 Outlook Express와 같은
메일클라이언트와 미리 정해진 규칙들을 사용하여 메일을 발송하게 된다. 이 정해진 규칙들을 SMTP프로토콜이라고 한다.
예를 들면, 윈도우 Outlook Express를 사용하여 메일을 보내기 위해서는 계정설정을 미리 해두어야하고, 그 계정정보를 보면 "보내는 메일
서버(SMTP 서버)"라는 곳이 있다. 아웃룩 익스프레스와 이 SMTP서버가 통신을 하는데에 쓰이는 프로토콜(통신규약)이 바로 SMTP프로토콜이
다.
SMTP프로토콜은 텍스트기반의 프로토콜이기 때문에, 일반 Telnet 프로그램으로 사용이 가능하다. 즉, 텔넷으로 메일서버에 연결해서 SMTP
프로토콜에 맞도록 명령만 내려주면 바로 메일이 발송된다는 말이다.
이런 작업들을 하기 위해서는 당연히 자신이 사용하는 메일서버가 있어야 한다. 이미 Outlook Express 등의 메일클라이언트를 사용하여 메
일을 주고받을 수 있다면, 그곳에 있는 메일계정에 있는 SMTP서버의 주소를 메모해두면 된다. 그런 메일서버가 있는지 없는지를 모른다면,
SMTP, POP3서비스를 무료로 제공하는 서비스에 가입을 하면 될 것이다. 그런곳에 가입을 하면 Outlook Express 설정하는 법을 알려주는데,
이때 SMTP서버의 주소를 메모해두면 된다. 간단히 엠파스나 네이버 등에서 POP3라고 검색하면 그런 서비스업체들을 쉽게 찾을 수 있다. 

1. settings에서 설정

* 댓글달고 바로 자동으로 이메일 발송
	* django signal 이용
	* http://dgkim5360.tistory.com/entry/django-signal-example 





##DAY13

#### .conf에서 settings_debug.json 생성
- facebook secret code 등등 보안상 위험한 정보들을 관리하기 위해 새로 json 파일을 만들어서 따로 보관
- gitignore를 사용해서 그 따로 관리한 파일을 github에 안보이게 관리

#### user가 올린 media file 저장위치 설정
- settings에 root 설정
- gitignore

#### PILLOW



##DAY14
