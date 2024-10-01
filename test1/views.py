from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
import os

def index(request):
    posts = Post.objects.all().order_by('created_at')
    
    # 각 포스트의 이미지가 동영상인지 아닌지 확인
    for post in posts:
        if post.image:
            ext = os.path.splitext(post.image.name)[1].lower()  # 파일 확장자 추출
            if ext in ['.mp4', '.webm', '.ogg','pdf']:
                post.is_video = True  # 동영상이면 True
            else:
                post.is_video = False  # 이미지이면 False
    
    return render(request, 'test1/index.html', {'posts': posts})


def single_post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 미디어 파일의 확장자를 확인
    media_extension = None
    if post.image:
        media_extension = os.path.splitext(post.image.name)[1].lower()  # 확장자 추출
    
    return render(request, 'test1/single_post_page.html', {
        'post': post,
        'media_extension': media_extension
    })

# 게시물 삭제 뷰
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    media = post.image
    
    if request.method == 'POST':  # POST 요청일 때만 삭제
        post.delete()  # 게시물 삭제
        return redirect('/test1/')  # 삭제 후 게시물 목록으로 리디렉션

    # GET 요청일 때는 삭제 확인 페이지 렌더링
    return render(request, 'test1/post_confirm_delete.html', {'post': post})

def make_new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        post = Post.objects.create(
            title = title,
            content= content,
            image= image,
        )
        return redirect('index')
    return render(
        request,'test1/create_post.html'
    )
import zipfile
import os
from django.http import HttpResponse

def download_all_files(request, pk):
    post = Post.objects.get(pk=pk)
    files = post.files.all()

    # 압축 파일을 만들기 위한 경로 설정
    zip_path = os.path.join(settings.MEDIA_ROOT, f'{post.title}_files.zip')

    # 압축 파일 생성
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for file in files:
            file_path = os.path.join(settings.MEDIA_ROOT, file.file.name)
            zip_file.write(file_path, file.file.name)

    # 압축 파일을 다운로드로 제공
    with open(zip_path, 'rb') as zip_file:
        response = HttpResponse(zip_file, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={post.title}_files.zip'
        return response
