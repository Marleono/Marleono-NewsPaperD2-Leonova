python manage.py shell

from news.models import Category

Category.objects.create(name="спорт")
Category.objects.create(name="музыка")
Category.objects.create(name="животные")
Category.objects.create(name="политика")
Category.objects.create(name="культура")
Category.objects.create(name="религия")

from django.contrib.auth import get_user_model
UserModel = get_user_model()
user1 = UserModel.objects.create_user("Test User1", password="foo")
user1.save()

user2 = UserModel.objects.create_user("Test User2", password="foo")
user2.save()

from news.models import Author
Author.objects.create(user=user1)
Author.objects.create(user=user2)

auth_1 = Author.objects.get(id=1)
auth_2 = Author.objects.get(id=2)

from news.models import Post
article1 = Post()
article1.author = auth_2
article1.post_type = article1.article
article1.title="Первая статья"
article1.text = "Это текст первой статьи"
article1.rating = 1
article1.save()

article2 = Post()
article2.author = auth_1
article2.post_type = article2.article
article1.title="Вторая статья"
article1.text = "Это текст второй статьи"
article1.rating = 2
article2.save()

article3 = Post()
article3.author = auth_1
article3.post_type = article2.news
article3.title="Первая НОВОСТЬ"
article3.text = "Это текст первой НОВОСТИ"
article3.rating = 1
article3.save()

cat1 = Category.objects.get(id=5)
cat2 = Category.objects.get(id=6)

from news.models import PostCategory

post_cat1 = PostCategory.objects.create(category=cat1, post=article1)
article1.category.all()
<QuerySet [<Category: Category object (5)>]>
post_cat2 = PostCategory.objects.create(category=cat2, post=article1)
article1.category.all()
<QuerySet [<Category: Category object (5)>, <Category: Category object (6)>]>
cat3 = Category.objects.get(id=4)
PostCategory.objects.create(category=cat3, post=article3)
cat4 = Category.objects.get(id=3)
cat5 = Category.objects.get(id=2)
PostCategory.objects.create(category=cat4, post=article2)
PostCategory.objects.create(category=cat5, post=article2)

from django.contrib.auth.models import User

user3 = User(username="Test User3",password="bar")
user3.save()

from news.models import (Comment, Post, Author)
from django.contrib.auth.models import User

comm1 = Comment()
comm1.post = Post.objects.get(id=1)
comm1.user = User.objects.get(id=1)
comm1.comment_text = "Первый коммент к первой статье"
comm1.save()

comm = Comment()
comm.post = Post.objects.get(id=1)
comm.user = User.objects.get(id=2)
comm.comment_text = "Второй коммент к первой статье"
comm.save()

comm3 = Comment()
comm3.post = Post.objects.get(id=1)
comm3.user = User.objects.get(id=3)
comm3.comment_text = "Третий коммент к первой статье"
comm.save()

comm = Comment()
comm.post = Post.objects.get(id=2)
comm.user = User.objects.get(id=1)
comm.comment_text = "Первый коммент ко второй статье"
comm.save()

comm = Comment()
comm.post = Post.objects.get(id=2)
comm.user = User.objects.get(id=2)
comm.comment_text = "Второй коммент ко второй статье"
comm.save()

comm.like()
comm.like()

comm = Comment.objects.get(id=1)
comm.like()

comm = Comment.objects.get(id=2)
comm.dislike()
comm.dislike()

post = Post.objects.get(id=3)
post.text = "dadljaldal a ldjajdajd akd;kw;ekqk kkjdajdjodj jdljsdljldjaldkmmelne oijoaijdoijojxLdmla ljlajdljadjajdjasdijwoiao oijojASJLjsDLKJALJjsajd ooajdj do
uaojdlajdljlj jaojdoajdljalkdqwoie"

post.save()
post.preview()

post.like()
post.like()
post.like()
post.like()
post.like()

post = Post.objects.get(id=2)
post.dislike()
post.dislike()
post.dislike()
post.dislike()

import news.models as m
a = m.Author.objects.get(id=2)
a.update_rating()
a = m.Author.objects.get(id=1)
a.update_rating()

author = m.Author.objects.all().order_by('-rating').first()
print(f'User name: "{author.user_id.username}"\nRating: {author.rating}')

max_rating = m.Post.objects.aggregate(max_rating=Max('rating'))['max_rating']
best_post = m.Post.objects.filter(rating=max_rating).first()
print(f'Best post id: {best_post.id}\nDate created: {best_post.created.date().isoformat()}\nAuthor: "{best_post.author_id.user_id.username}"\nRating: {best_post.rating}\nTitle: {best_post.title}\nText preview: {best_post.preview()}')

item = 0
for comment in comments:
 item += 1
 print(f'item #{item}\nDate created: {comment.created.date().isoformat()}\nUser: {comment.user_id.username}\nRating: {comment.rating}\nText: {comment.text}\n-------------------------')